from functools import wraps
import psycopg2


def transaction(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            database="rocket_bank",
            user="postgres",
            password="root",
            host="localhost"
        )
        cursor = conn.cursor()
        
        try:
            result = function(cursor=cursor, *args, **kwargs)
            conn.commit()
            return result
        finally:
            cursor.close()
            conn.close()
            
    return wrapper