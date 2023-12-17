from models.utils import transaction
from datetime import datetime

@transaction
def getPayments(id, cursor):
    cursor.execute('SELECT * FROM payment INNER JOIN person ON payment.sender_id =person.id WHERE receiver_id = {}'.format(id))
    Entredas = cursor.fetchall()

    cursor.execute('SELECT * FROM payment INNER JOIN person ON payment.receiver_id = person.id WHERE sender_id = {}'.format(id))
    Saidas = cursor.fetchall()

    payments = {'Entradas': Entredas, 'Saidas': Saidas}
    return payments

#Tem que testar essa função
@transaction
def setPayment(cursor,receiver_id,sender_id,value):
    cursor.execute('INSERT INTO payment(sender_id,receiver_id,value,date) VALUES({0},{1},{2},{3})'.format(sender_id,receiver_id,value,datetime.today()))
    cursor.execute('UPDATE SET stored_value=stored_value + {} WHERE receiver_id=id'.format(value))
    cursor.execute('UPDATE SET stored_value=stored_value - {} WHERE sender_id=id)'.format(value))
