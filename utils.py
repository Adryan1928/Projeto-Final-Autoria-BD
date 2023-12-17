from models.utils import transaction

@transaction
def getPayments(cursor, id):
    cursor.execute('')
    return payments