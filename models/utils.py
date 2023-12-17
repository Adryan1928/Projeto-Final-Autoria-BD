from functools import wraps
import psycopg2
import psycopg2.extras


def transaction(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            database="rocket_bank",
            user="postgres",
            password="1234567k",
            host="localhost"
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        try:
            result = function(cursor=cursor, *args, **kwargs)
            conn.commit()
            return result
        finally:
            cursor.close()
            conn.close()
            
    return wrapper