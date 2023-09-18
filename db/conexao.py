import sqlite3
import os

def criar_conexao():
    if not os.path.exists('pizzaria.db'):
        conn = sqlite3.connect('pizzaria.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        categoria_id INTEGER,
        preco REAL NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categorias (id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT,
            endereco TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            data_hora DATETIME,
            status TEXT CHECK(status IN ('aceito', 'producao', 'entregue')),
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS itens_pedido (
            id INTEGER PRIMARY KEY,
            pedido_id INTEGER,
            produto_id INTEGER,
            quantidade INTEGER,
            FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY,
            pedido_id INTEGER,
            valor REAL,
            FOREIGN KEY (pedido_id) REFERENCES pedidos (id)
        )
        ''')

        conn.commit()
        conn.close()

    conn = sqlite3.connect('pizzaria.db')
    return conn