import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from db.conexao import criar_conexao

class ProdutoTela:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciar Produtos")
        self.root.geometry("800x600")

        # Crie uma Treeview para exibir os produtos
        self.treeview = ttk.Treeview(self.root, columns=("ID", "Nome", "Categoria"))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Nome")
        self.treeview.heading("#3", text="Categoria")
        self.treeview.pack()

        # Botão para adicionar produtos
        self.button_adicionar = tk.Button(self.root, text="Adicionar Produto", command=self.adicionar_produto)
        self.button_adicionar.pack()

        # Preencha a Treeview com dados de produtos
        self.preencher_treeview()

    def preencher_treeview(self):
        # Preencha a Treeview com dados reais do banco de dados ou de onde quer que você os obtenha
        # Use a função `insert` para adicionar produtos à Treeview
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT produtos.id, produtos.nome, categorias.nome FROM produtos JOIN categorias ON produtos.categoria_id = categorias.id")
        produtos = cursor.fetchall()
        conn.close()

        # Limpe a Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Adicione os produtos à Treeview
        for produto in produtos:
            produto_id, nome, categoria = produto
            self.treeview.insert("", "end", values=(produto_id, nome, categoria))

    def adicionar_produto(self):
        # Crie uma nova janela para adicionar produto
        adicionar_produto_window = tk.Toplevel(self.root)
        adicionar_produto_window.title("Adicionar Produto")

        adicionar_produto_window.iconbitmap("pizza.ico")

        # Label e campo de entrada para o nome do produto
        label_nome = tk.Label(adicionar_produto_window, text="Nome do Produto:")
        label_nome.pack()

        entry_nome = tk.Entry(adicionar_produto_window)
        entry_nome.pack()

        # Label e campo de seleção para a categoria
        label_categoria = tk.Label(adicionar_produto_window, text="Categoria:")
        label_categoria.pack()

        # Crie uma variável de tkinter para armazenar a categoria selecionada
        categoria_selecionada = tk.StringVar()

        # Recupere as categorias do banco de dados
        categorias = self.obter_categorias_do_banco()  # Implemente esta função

        # Crie um widget de Opção para selecionar a categoria
        dropdown_categoria = tk.OptionMenu(adicionar_produto_window, categoria_selecionada, *categorias)
        dropdown_categoria.pack()

        # Label e campo de entrada para o preço do produto
        label_preco = tk.Label(adicionar_produto_window, text="Preço:")
        label_preco.pack()

        entry_preco = tk.Entry(adicionar_produto_window)
        entry_preco.pack()

        # Botão "OK" para adicionar o produto
        botao_ok = tk.Button(adicionar_produto_window, text="OK", command=lambda: self.cadastrar_produto(entry_nome.get(), categoria_selecionada.get(), entry_preco.get(), adicionar_produto_window))
        botao_ok.pack()

    # ...

    def obter_categorias_do_banco(self):
        # Consulte o banco de dados para obter a lista de categorias
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM categorias")
        categorias = [row[0] for row in cursor.fetchall()]
        conn.close()
        return categorias


    def cadastrar_produto(self, nome_produto, categoria, preco, janela):
        if nome_produto and categoria and preco:
            # Convertemos o preço para um valor float
            preco = float(preco)

            # Aqui, você deve obter o ID da categoria selecionada com base no nome da categoria
            # Suponhamos que você tenha uma função que faz isso chamada 'obter_id_categoria'
            categoria_id = self.obter_id_categoria(categoria)

            # Insira o produto no banco de dados com nome, categoria_id e preço
            conn = criar_conexao()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO produtos (nome, categoria_id, preco) VALUES (?, ?, ?)", (nome_produto, categoria_id, preco))
            conn.commit()
            conn.close()

            # Atualize a Treeview para refletir o novo produto
            self.preencher_treeview()

            # Feche a janela de adicionar produto
            janela.destroy()

    def obter_id_categoria(self, nome_categoria):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM categorias WHERE nome = ?", (nome_categoria,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return resultado[0]
        else:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ProdutoTela(root)
    root.mainloop()
