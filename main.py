import os
from flask import Flask, render_template, request
from controllers.users import auth


app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos/<int:id>/')
def pagamentos(id):

    return render_template('pagamentos.html', post = id)

@app.route('/extrato/<int:id>/')
def extrato(id):
    return render_template('extrato.html')

@app.route('/pix/', methods=['GET', 'POST'])
def pix():
    if request.args.get('step') == 'select' or not request.args.get('step'):
        return render_template('pix.html')
    elif request.args.get('step') == 'confirm':
        return render_template('pix_confirm.html')
