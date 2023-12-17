from models.utils import transaction

@transaction
def getPayments(cursor, id):
    cursor.execute('SELECT * FROM payment WHERE receiver_id = {}'.format(id))
    Entredas = cursor.fetchall()

    cursor.execute('SELECT * FROM payment WHERE sender_id = {}'.format(id))
    Saidas = cursor.fetchall()

    payments = {'Entradas': Entredas, 'Saidas': Saidas}
    return payments