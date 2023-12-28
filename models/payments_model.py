from models.utils import transaction
from datetime import date

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
def setPayment(sender_id, receiver_id, value, cursor):
    cursor.execute('INSERT INTO payment(sender_id,receiver_id,value) VALUES({0},{1},{2});'.format(sender_id,receiver_id,value))
    cursor.execute('UPDATE person SET stored_value=stored_value + {} WHERE id={};'.format(value, receiver_id))
    cursor.execute('UPDATE person SET stored_value=stored_value - {} WHERE id={};'.format(value, sender_id))
