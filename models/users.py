from .utils import transaction


class User():
    def __init__(self, data):
        self.id = data.get('id', None)
        self.name = data['name']
        self.phone_number = data['phone_number']
        self.email = data['email']
        self.cpf = data['cpf']
        self.birth_date = data['birth_date']
        self.password = data['password']
        
    @staticmethod
    @transaction
    def get_user_by_pix(cursor, pix_key):
        cursor.execute('SELECT * FROM Person '
                       'INNER JOIN Pix '
                       'ON Pix.person_id = Person.id '
                       'WHERE Pix.key = %s;', (pix_key,))
        user = cursor.fetchone()
        return user

    @staticmethod
    @transaction
    def get_user_by_email(*, cursor, email):
        cursor.execute('SELECT * FROM PERSON WHERE EMAIL = %s;', (email,))
        user = cursor.fetchone()
        return user
    
    @transaction
    def is_unique(self, cursor):
        cursor.execute('SELECT * FROM PERSON WHERE EMAIL = %s OR CPF = %s;', (self.email, self.cpf,))
        user = cursor.fetchone()        
        return user is None
        
    @transaction
    def save(self, cursor):
        cursor.execute('INSERT INTO Person (name, phone_number, email, cpf, birth_date, password) '
                       'VALUES (%s, %s, %s, %s, %s, %s);',
                       (self.name, self.phone_number, self.email, self.cpf, self.birth_date, self.password))
