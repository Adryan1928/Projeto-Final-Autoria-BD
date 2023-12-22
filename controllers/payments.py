from flask import Blueprint, redirect, render_template, request, url_for

import models.favorites as favorites

from models.users import User

import utils

payments = Blueprint('payments', __name__, static_folder='static', template_folder='templates')

@payments.route('/<int:id>/', methods=['GET', 'POST'])
def show_payments(id):
    if request.method == 'GET':
        payments_context = utils.getPayments(id)
        user = User.get_user_by_id(id)
        user_favorites = favorites.getFavorites(id=id)
        return render_template('pagamentos.html', favorites=user_favorites, user = user, post = id, payments=payments_context)
    else:
        type = request.form.get('type') 
        name = request.form.get('name')
        key = request.form.get('key')

        favorites.add_favorite(key=key, user_id=id)
        return redirect(url_for('payments.show_payments', id=id))
    
@payments.route('/excluir_favorito/<int:id>/')
def delete_favorite(id):
    user_favorites = favorites.getFavorite(id=id)
    favorites.deleteFavorites(id=id)
    return redirect(url_for('payments.show_payments', id=user_favorites['person_id']))
