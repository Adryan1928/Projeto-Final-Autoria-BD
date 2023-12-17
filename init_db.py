import psycopg2
conn = psycopg2.connect(database="rocket_bank",
                        user="postgres",
                        password="root",
                        host="localhost")

cursor = conn.cursor()



cursor.execute('CREATE TABLE IF NOT EXISTS Person (id SERIAL PRIMARY KEY,'
                'name VARCHAR(255) NOT NULL,'
                'number int NOT NULL,'
                'email VARCHAR(50) NOT NULL,'
                'CPF VARCHAR(11) UNIQUE NOT NULL,'
                'birth_date DATE NOT NULL,'
                'password VARCHAR(20) NOT NULL);')

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