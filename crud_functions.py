import sqlite3

def dbTableIsEmpty(tbl: str):
    with sqlite3.connect('Products.db') as connection:
        cursor = connection.cursor()
        return cursor.execute(f'SELECT COUNT(*) FROM {tbl}').fetchone()[0] == 0

def initiate_db_products():
    with sqlite3.connect('Products.db') as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products(
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL,
                    picture TEXT NOT NULL
                )
            """)

        if dbTableIsEmpty('Products'):
            for i in range(1, 5):
                cursor.execute(
                    'INSERT INTO Products (title, description, price, picture) VALUES (?,?,?,?)',
                    (f'Product{i}', f'Описание Product{i}', f'{i * 100}', f'product_images/{i}.jpg'))

def get_all_products():
    with sqlite3.connect('Products.db') as connection:
        cursor = connection.cursor()
        products = cursor.execute('SELECT * FROM Products')
        return products

def initiate_db_users():
    with sqlite3.connect('Users.db') as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER NOT NULL
                )
            """)

def add_user(username, email, age):
    with sqlite3.connect('Users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?,?,?, 1000)",
            (username, email, age))


def is_included(username):
    connection = sqlite3.connect("Users.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    user_exists = cursor.fetchone()[0] > 0

    connection.close()
    return user_exists
