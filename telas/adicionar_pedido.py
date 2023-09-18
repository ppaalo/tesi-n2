import tkinter as tk
from tkinter import messagebox

class AdicionarPedido:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Adicionar Pedido")
        self.root.geometry("800x600")
        self.root.iconbitmap("pizza.ico")

        # Crie a interface gráfica para adicionar pedidos aqui, por exemplo:
        label = tk.Label(self.root, text="Informações do Pedido:")
        label.pack()

        entry_cliente = tk.Entry(self.root, width=50)
        entry_cliente.pack()

        button_salvar = tk.Button(self.root, text="Salvar Pedido", command=self.salvar_pedido)
        button_salvar.pack()

        self.root.mainloop()

    def salvar_pedido(self):
        # Lógica para salvar o pedido no banco de dados (use a conexão SQLite aqui)
        # Depois de salvar o pedido, você pode exibir uma mensagem de sucesso ou fazer o que for necessário.
        messagebox.showinfo("Sucesso", "Pedido salvo com sucesso!")

if __name__ == "__main__":
    app = AdicionarPedido()
