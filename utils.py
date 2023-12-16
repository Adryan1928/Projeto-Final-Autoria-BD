import psycopg2
import psycopg2.extras
conn = psycopg2.connect(database="rocket_bank",
                        user="postgres",
                        password="root",
                        host="localhost")

cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
def getFavorites(id):
    cursor.execute('SELECT * FROM favorite INNER JOIN pix ON pix.id = favorite.pix_id INNER JOIN person ON favorite.person_id = person.id WHERE favorite.person_id = {};'.format(id))
    favorites = cursor.fetchall()
    return favorites