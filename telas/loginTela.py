import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from db.conexao import criar_conexao
import time
from telas.menuTela import criar_tela_menu

def fazer_login():
    username = entry_username.get()
    password = entry_password.get()

    conn = criar_conexao()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login", "Login bem-sucedido")
        criar_tela_menu()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos")

    conn.close()

def atualizar_relogio():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%d/%m/%Y")
    relogio.config(text=f"{current_time}\n{current_date}")
    relogio.after(1000, atualizar_relogio)  # Atualiza a cada 1 segundo

def criar_tela_login():
    root = tk.Tk()
    root.title("Pizzaria Login")
    root.geometry("600x400")
    root.iconbitmap("pizza.ico")

    style = Style(theme='superhero')

    global relogio
    relogio = tk.Label(root, text="", font=("Helvetica", 12))
    relogio.place(x=10, y=10)

    label_username = tk.Label(root, text="Usuário:")
    label_username.pack()
    global entry_username
    entry_username = tk.Entry(root)
    entry_username.pack()

    label_password = tk.Label(root, text="Senha:")
    label_password.pack()
    global entry_password
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    login_button = tk.Button(root, text="Login", command=fazer_login, bg=style.colors.get("success"))
    login_button.pack()
    atualizar_relogio()

    root.mainloop()

if __name__ == "__main__":
    criar_tela_login()
