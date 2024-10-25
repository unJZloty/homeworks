import sqlite3

def add_products():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()

    sample_data = [
        ("Продукт 1", "Описание 1", 100),
        ("Продукт 2", "Описание 2", 200),
        ("Продукт 3", "Описание 3", 300),
        ("Продукт 4", "Описание 4", 400),
    ]

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       sample_data)

    conn.commit()
    conn.close()

add_products()
