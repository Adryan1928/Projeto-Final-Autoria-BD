from functools import wraps
import os
import psycopg2
import psycopg2.extras


def transaction(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(database=os.getenv('DATABASE_NAME'),
                                user=os.getenv('DATABASE_USER'),
                                password=os.getenv('DATABASE_PASSWORD'),
                                host=os.getenv("DATABASE_HOST"))

        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        try:
            result = function(cursor=cursor, *args, **kwargs)
            conn.commit()
            return result
        finally:
            cursor.close()
            conn.close()
            
    return wrapper