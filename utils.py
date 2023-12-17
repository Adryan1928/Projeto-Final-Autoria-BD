import psycopg2
import psycopg2.extras
conn = psycopg2.connect(database="rocket_bank",
                        user="postgres",
                        password="root",
                        host="localhost")

def getFavorite(id):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM favorite WHERE favorite_id = {};'.format(id))
    favorite = cursor.fetchone()
    cursor.close()
    return favorite

def getFavorites(id):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM favorite INNER JOIN pix ON pix.id = favorite.pix_id INNER JOIN person ON favorite.person_id = person.id WHERE favorite.person_id = {};'.format(id))
    favorites = cursor.fetchall()
    print(favorites)
    cursor.close()
    return favorites

def setFavorites(key):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    pix = getPix(key)
    person_id = pix[0]['person_id']
    pix_id = pix[0]['id']
    cursor.execute('INSERT INTO favorite(person_id, pix_id) VALUES (({0})::integer, ({1})::integer) ;'.format(person_id, pix_id))
    conn.commit()
    cursor.close()

def deleteFavorites(id):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute('DELETE FROM favorite WHERE favorite_id = {};'.format(id))
    conn.commit()
    cursor.close()

def getPix(key):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM pix WHERE pix.key = ({})::name;'.format(key))
    pix = cursor.fetchall()
    cursor.close()
    return pix