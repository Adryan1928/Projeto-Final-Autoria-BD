from flask import Flask, render_template, request, redirect, url_for
import utils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos/<int:id>/', methods=['GET', 'POST'])
def pagamentos(id):
    if request.method == 'GET':
        favorites = utils.getFavorites(id)
        return render_template('pagamentos.html', posts=favorites)
    else:
        type = request.form.get('type') 
        name = request.form.get('name')
        key = request.form.get('key')

        utils.setFavorites(name=name, key=key, type=type)
        return redirect(url_for('pagamentos', id=1))
    

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/pix', methods=['GET', 'POST'])
def pix():
    if request.args.get('step') == 'select' or not request.args.get('step'):
        return render_template('pix.html')
    elif request.args.get('step') == 'confirm':
        return render_template('pix_confirm.html')
