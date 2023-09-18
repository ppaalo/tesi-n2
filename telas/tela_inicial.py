import tkinter as tk
from tkinter import Menu
from db.conexao import criar_conexao
from telas.categoriaTela import CategoriaTela
from telas.produtoTela import ProdutoTela

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Inicial")
        self.root.geometry("800x600")

        # Crie a interface gráfica
        self.frame_pedidos = tk.Frame(self.root)
        self.frame_pedidos.pack()

        # Crie um MenuBar
        menubar = Menu(root)
        root.config(menu=menubar)

        # Menu "Produtos" com a opção "Adicionar Categoria" e "Adicionar Produto"
        produtos_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Produtos", menu=produtos_menu)
        produtos_menu.add_command(label="Adicionar Categoria", command=self.adicionar_categoria)
        produtos_menu.add_command(label="Adicionar Produto", command=self.adicionar_produto)

        clientes_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Pedidos", menu=clientes_menu)
        clientes_menu.add_command(label="Clientes", command=self.adicionar_cliente)
        clientes_menu.add_command(label="Historico", command=self.historico_cliente)



        self.treeview_pedidos = tk.Text(self.frame_pedidos)
        self.treeview_pedidos.pack()

    def atualizar_pedidos(self):
        # Limpe a lista de pedidos existente
        self.treeview_pedidos.delete("1.0", tk.END)

        # Consulta o banco de dados para obter pedidos com status "aceito" e "producao"
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE status IN ('aceito', 'producao')")
        pedidos = cursor.fetchall()
        conn.close()

        # Adicione os pedidos à Treeview
        for pedido in pedidos:
            pedido_id, status = pedido[0], pedido[3]
            self.treeview_pedidos.insert(tk.END, f"Pedido {pedido_id}\nStatus: {status}\n\n")

    def adicionar_categoria(self):
        categoria_window = tk.Tk()
        categoria_window.title("Tela de Categorias")
        categoria_window.geometry("800x600")
        categoria_tela = CategoriaTela(categoria_window)

    def adicionar_produto(self):
        produto_window = tk.Tk()
        produto_window.title("Tela de Categorias")
        produto_window.geometry("800x600")
        categoria_tela = ProdutoTela(produto_window)
    
    def adicionar_cliente(self):

        pass

    def historico_cliente(self):

        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()
