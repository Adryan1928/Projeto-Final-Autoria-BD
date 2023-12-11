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

cursor.execute('CREATE TABLE IF NOT EXISTS Payment (id SERIAL PRIMARY KEY,'
                'id_sender int NOT NULL,'
                'id_receiver int NOT NULL,'
                'value float NOT NULL,'
                'date DATE NOT NULL);')

cursor.execute('CREATE TABLE IF NOT EXISTS Favorite (id SERIAL PRIMARY KEY,'
                'id_user int NOT NULL,'
                'id_favorite int NOT NULL,'
                'pix VARCHAR(255) NOT NULL);')

cursor.execute('ALTER TABLE Payment '
                'ADD FOREIGN KEY (id_sender) REFERENCES Person(id); '
                'ALTER TABLE Payment '
                'ADD FOREIGN KEY (id_receiver) REFERENCES Person(id);')

cursor.execute('ALTER TABLE Favorite '
                'ADD FOREIGN KEY (id_user) REFERENCES Person(id); '
                'ALTER TABLE Favorite '
                'ADD FOREIGN KEY (id_favorite) REFERENCES Person(id);')

conn.commit()
cursor.close()
conn.close()