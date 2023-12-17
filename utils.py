import psycopg2
import psycopg2.extras
conn = psycopg2.connect(database="rocket_bank",
                        user="postgres",
                        password="root",
                        host="localhost")


def getFavorites(id):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM favorite INNER JOIN pix ON pix.id = favorite.pix_id INNER JOIN person ON favorite.person_id = person.id WHERE favorite.person_id = {};'.format(id))
    favorites = cursor.fetchall()
    cursor.close()
    return favorites

def setFavorites(key, name, type):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    pix = getPix(key)
    person_id = pix[0]['person_id']
    pix_id = pix[0]['id']
    print(person_id, pix_id)
    cursor.execute('INSERT INTO favorite(person_id, pix_id) VALUES (({0})::integer, ({1})::integer) ;'.format(person_id, pix_id))
    conn.commit()
    cursor.close()

def getPix(key):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM pix WHERE pix.key = ({})::name;'.format(key))
    pix = cursor.fetchall()
    cursor.close()
    return pix