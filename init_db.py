import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("insert into posts (title, content) values (?, ?)",
            ('Первый пост', ' Содержание первого поста'))

cur.execute("insert into posts (title, content) values (?, ?)",
            ('Второй пост', 'Содержание второго поста'))

connection.commit()
connection.close()