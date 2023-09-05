import sqlite3
import os

def criar_conexao():
    if not os.path.exists('pizzaria.db'):
        conn = sqlite3.connect('pizzaria.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE usuarios
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT NOT NULL,
                           password TEXT NOT NULL)''')
        
        cursor.execute('''CREATE TABLE menu
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome TEXT NOT NULL,
                           descricao TEXT,
                           categoria TEXT NOT NULL,
                           preco REAL NOT NULL)''')

        # Insira o usuário de exemplo "admin" com a senha "admin"
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", ("admin", "admin"))

        conn.commit()
        conn.close()

    conn = sqlite3.connect('pizzaria.db')
    return conn
