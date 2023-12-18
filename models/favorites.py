import psycopg2
import psycopg2.extras
conn = psycopg2.connect(database="rocket_bank",
                        user="postgres",
                        password="root",
                        host="localhost")

from models.utils import transaction

@transaction
def getFavorite(*, cursor, id):
    cursor.execute('SELECT * FROM favorite WHERE favorite_id = {};'.format(id))
    favorite = cursor.fetchone()
    return favorite

@transaction
def getFavorites(*, cursor, id):
    cursor.execute('SELECT * FROM favorite INNER JOIN pix ON pix.id = favorite.pix_id INNER JOIN person ON favorite.person_id = person.id WHERE favorite.person_id = {};'.format(id))
    favorites = cursor.fetchall()
    return favorites

@transaction
def add_favorite(*, cursor, user_id, key):
    pix = get_pix_by_key(key=key)
    pix_id = pix['id']
    cursor.execute('INSERT INTO favorite(person_id, pix_id) VALUES (({0})::integer, ({1})::integer) ;'.format(user_id, pix_id))

@transaction
def deleteFavorites(*, cursor, id):
    cursor.execute('DELETE FROM favorite WHERE favorite_id = {};'.format(id))

@transaction
def get_pix_by_key(*, cursor, key):
    cursor.execute('SELECT * FROM pix WHERE pix.key = ({})::name;'.format(key))
    pix = cursor.fetchone()
    return pix
