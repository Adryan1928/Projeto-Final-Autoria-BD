import psycopg2
import psycopg2.extras
import datetime
conn = psycopg2.connect(database="rocket_bank",
                        user="postgres",
                        password="root",
                        host="localhost")
    
def payment(receiver_id,sender_id,value):
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute('INSERT INTO payment(sender_id,receiver_id,value,date) VALUES({0},{1},{2},{3})'.format(sender_id,receiver_id,value,date.today()))
    cursor.execute('UPDATE SET stored_value=stored_value + value WHERE receiver_id=id'.format(value))
    cursor.execute('UPDATE SET stored_value=stored_value - value WHERE sender_id=id)'.format(value))
    print("payment done!")
    conn.commit()
    cursos.close()




