import datetime
import unittest
from utils import transaction
from users import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User({
            'name': 'Test User',
            'number': 123456789,
            'email': 'test@example.com',
            'cpf': '12345678902',
            'birth_date': datetime.date.today(),
            'password': 'password'
        })

    @transaction
    def test_save(self, cursor):
        self.user.save()
        
        cursor.execute('SELECT * FROM Person WHERE cpf = %s', (self.user.cpf,))
        result = cursor.fetchone()
        
        self.assertEqual(result[1], self.user.name)
        self.assertEqual(result[2], self.user.number)
        self.assertEqual(result[3], self.user.email)
        self.assertEqual(result[4], self.user.cpf)
        self.assertEqual(result[5], self.user.birth_date)
        self.assertEqual(result[6], self.user.password)


if __name__ == '__main__':
    unittest.main()