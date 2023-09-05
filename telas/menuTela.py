import tkinter as tk
from tkinter import ttk
from db.conexao import criar_conexao

def exibir_menu():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        card_frame = tk.Frame(menu_frame, relief="solid", borderwidth=2)
        card_frame.pack(side="left", padx=10, pady=10)

        nome, descricao, categoria, preco = row[1:]

        nome_label = tk.Label(card_frame, text=nome, font=("Helvetica", 12, "bold"))
        nome_label.pack(pady=(10, 5))

        descricao_label = tk.Label(card_frame, text=descricao)
        descricao_label.pack()

        categoria_label = tk.Label(card_frame, text=categoria)
        categoria_label.pack()

        preco_label = tk.Label(card_frame, text=f"Preço: R${preco:.2f}", font=("Helvetica", 12, "bold"))
        preco_label.pack(pady=5)

def criar_tela_menu():
    root = tk.Tk()
    root.title("Menu da Pizzaria")

    conn = criar_conexao()
    cursor = conn.cursor()

    global menu_frame
    menu_frame = ttk.Frame(root)
    menu_frame.pack(padx=20, pady=20)

    exibir_menu()

    root.mainloop()

if __name__ == "__main__":
    criar_tela_menu()
