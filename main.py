import os
from flask import Flask, render_template, request, redirect, url_for
import utils
from controllers.users import auth


app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.secret_key = os.environ.get('SECRET_KEY')

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

        utils.setFavorites(key=key)
        return redirect(url_for('pagamentos', id=1))
    
@app.route('/pagamentos/excluir_favorito/<int:id>/')
def delete_favorite(id):
    favorito = utils.getFavorite(id)
    utils.deleteFavorites(id)
    return redirect(url_for('pagamentos', id=favorito['person_id']))

@app.route('/pix', methods=['GET', 'POST'])
def pix():
    if request.args.get('step') == 'select' or not request.args.get('step'):
        return render_template('pix.html')
    elif request.args.get('step') == 'confirm':
        return render_template('pix_confirm.html')
