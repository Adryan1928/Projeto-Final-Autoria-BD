import psycopg2
import os

conn = psycopg2.connect(database=os.getenv('DATABASE_NAME'),
                        user=os.getenv('DATABASE_USER'),
                        password=os.getenv('DATABASE_PASSWORD'),
                        host=os.getenv("DATABASE_HOST"))

cursor = conn.cursor()



cursor.execute('CREATE TABLE IF NOT EXISTS Person (id SERIAL PRIMARY KEY,'
                'name VARCHAR(255) NOT NULL,'
                'phone_number VARCHAR(15) NOT NULL,'
                'email VARCHAR(256) UNIQUE NOT NULL,'
                'CPF VARCHAR(11) UNIQUE NOT NULL,'
                'birth_date DATE NOT NULL,'
                'password VARCHAR(20) NOT NULL,'
                'stored_value FLOAT NOT NULL);')

cursor.execute('CREATE TABLE IF NOT EXISTS Pix ('
                'id SERIAL PRIMARY KEY,'
                'person_id INTEGER NOT NULL,'
                'type VARCHAR(10) NOT NULL,'
                'key VARCHAR(256) UNIQUE NOT NULL);')

cursor.execute('CREATE TABLE IF NOT EXISTS Payment (id SERIAL PRIMARY KEY,'
                'sender_id int NOT NULL,'
                'receiver_id int NOT NULL,'
                'value float NOT NULL,'
                'date DATE NOT NULL);')

cursor.execute('CREATE TABLE IF NOT EXISTS Favorite (favorite_id SERIAL PRIMARY KEY,'
                'person_id int NOT NULL,'
                'pix_id int NOT NULL);')

cursor.execute('ALTER TABLE Pix '
                'ADD FOREIGN KEY (person_id) REFERENCES Person(id); ')

cursor.execute('ALTER TABLE Payment '
                'ADD FOREIGN KEY (sender_id) REFERENCES Person(id); '
                'ALTER TABLE Payment '
                'ADD FOREIGN KEY (receiver_id) REFERENCES Person(id);')

cursor.execute('ALTER TABLE Favorite '
                'ADD FOREIGN KEY (person_id) REFERENCES Person(id); '
                'ALTER TABLE Favorite '
                'ADD FOREIGN KEY (pix_id) REFERENCES Pix(id);')

conn.commit()
cursor.close()
conn.close()