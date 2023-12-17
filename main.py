import os
from flask import Flask, render_template, request, redirect, url_for
from controllers.users import auth
import utils


app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos/<int:id>/')
def pagamentos(id):
    payments = utils.getPayments(id)
    return render_template('pagamentos.html', post = id, posts = payments)

@app.route('/extrato/<int:id>/', methods=['GET', 'POST'])
def extrato(id):
    payments = utils.getPayments(id)
    if request.method == 'POST':
        text = request.form.get('filtro')
        if len(text.strip()) == 0:
            return render_template('extrato.html', post=id, posts=payments)
        
        payments_filtrado = {'Entradas': [], 'Saidas': []}
        for en_sa in payments:
            for payment in payments[en_sa]:
                if payment['name'] == text:
                    payments_filtrado[en_sa].append(payment)
        
        return render_template('extrato.html', post=id, posts=payments_filtrado)
    
    return render_template('extrato.html', post=id, posts=payments)

@app.route('/pix/', methods=['GET', 'POST'])
def pix():
    if request.args.get('step') == 'select' or not request.args.get('step'):
        return render_template('pix.html')
    elif request.args.get('step') == 'confirm':
        return render_template('pix_confirm.html')
