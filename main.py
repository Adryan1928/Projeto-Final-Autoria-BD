import os
from flask import Flask, render_template, request, redirect, url_for

from controllers.users import auth
from controllers.payments import payments
import utils
from models.users import User


app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(payments, url_prefix='/payments')
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')


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

@app.route('/depositos/<int:id>/', methods=['GET', 'POST'])
def depositos(id):
    print(request.method)
    if request.method == 'POST':
        valor = request.form.get('valor')
        senha = request.form.get('senha')
        user = User.get_user_by_id(id)
        if senha == user['password']:
            print('chega aqui?')
            User.deposito(id=id, value=valor)
            return redirect(url_for('pagamentos.pagamentos', id=id))
    return render_template('depositos.html', post=id)

@app.route('/pix/', methods=['GET', 'POST'])
def pix():
    if request.args.get('step') == 'select' or not request.args.get('step'):
        return render_template('pix.html')
    elif request.args.get('step') == 'confirm':
        return render_template('pix_confirm.html')
