import psycopg2  # Для работы с PostgreSQL
from pymongo import MongoClient

from .forms import RegisterForm, LoginForm

uri = "mongodb+srv://web17_mod8:IDkrkN1JmruWcbSb@web17.k2uu2ec.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client.quotes_db
users_collection = db['users']

postgres_conn = psycopg2.connect(
        database='quotes_db',
        user='postgres',
        password='t5r4e3w2Q!',
        host='localhost',
        port='5432'
    )
postgres_cursor = postgres_conn.cursor()

def create_users_table():
    postgres_cursor.execute('''CREATE TABLE IF NOT EXISTS users_from_mongo (
                id VARCHAR(100) PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        ''')
    

def migrate_to_postgres():
    
    mongo_data = list(users_collection.find())
    create_users_table()

    for data in mongo_data:
        postgres_cursor.execute('''INSERT INTO users_from_mongo (id, username, email, password) VALUES (%s, %s, %s, %s) 
                                WHERE NOT EXISTS (SELECT 1 FROM users_from_mongo WHERE id = %s)''', 
            (str(data['_id']),
            data['username'],
            data['email'],
            data['password'])
        )
        

    postgres_conn.commit()

    client.close()
    postgres_cursor.close()
    postgres_conn.close()
