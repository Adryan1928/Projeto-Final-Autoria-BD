from flask import Blueprint, redirect, render_template, request, url_for

import models.favorites as favorites

from models.users import User

payments = Blueprint('payments', __name__, static_folder='static', template_folder='templates')

@payments.route('/<int:id>/', methods=['GET', 'POST'])
def get_payments(id):
    if request.method == 'GET':
        user = User.get_user_by_id(id)
        user_favorites = favorites.getFavorites(id=id)
        return render_template('pagamentos.html', posts=user_favorites, user = user, post = id)
    else:
        type = request.form.get('type') 
        name = request.form.get('name')
        key = request.form.get('key')

        favorites.add_favorite(key=key, user_id=id)
        return redirect(url_for('payments.get_payments', id=1))
    
@payments.route('/excluir_favorito/<int:id>/')
def delete_favorite(id):
    user_favorites = favorites.getFavorite(id=id)
    favorites.deleteFavorites(id=id)
    return redirect(url_for('payments.get_payments', id=user_favorites['person_id']))
