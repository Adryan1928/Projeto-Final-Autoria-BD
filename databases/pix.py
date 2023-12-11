import psycopg2
conn = psycopg2.connect(database="rocket_bank",
                        user="postgres",
                        password="root",
                        host="localhost")
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Pix ('
                'id SERIAL PRIMARY KEY,'
                'person_id INTEGER NOT NULL,'
                'type VARCHAR(10) NOT NULL,'
                'key VARCHAR(256) NOT NULL, '
                
                'ADD FOREIGN KEY (person_id) REFERENCES Person(id)')

conn.commit()
cursor.close()
conn.close()