import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from db.conexao import criar_conexao

class CategoriaTela:
    def __init__(self, root):
        self.root = root
        self.root.title("Categoria")
        self.root.geometry("800x600")
        self.root.iconbitmap("pizza.ico")

        self.treeview = ttk.Treeview(self.root, columns=("ID", "Nome"))
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Nome")
        self.treeview.pack()

        # Botões
        self.button_adicionar = tk.Button(self.root, text="Adicionar Categoria", command=self.adicionar_categoria)
        self.button_adicionar.pack()

        self.button_editar = tk.Button(self.root, text="Editar Categoria", command=self.editar_categoria)
        self.button_editar.pack()

        self.button_excluir = tk.Button(self.root, text="Excluir Categoria", command=self.excluir_categoria)
        self.button_excluir.pack()

        # Preencher a Treeview com dados de categorias (substitua com seus dados reais)
        self.preencher_treeview()

    def preencher_treeview(self):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        conn.close()

        # Limpe a Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Adicione as categorias à Treeview
        for categoria in categorias:
            categoria_id, nome = categoria
            self.treeview.insert("", "end", values=(categoria_id, nome))

    def adicionar_categoria(self):
        # Crie uma nova janela para adicionar categoria
        adicionar_categoria_window = tk.Toplevel(self.root)
        adicionar_categoria_window.title("Adicionar Categoria")
        adicionar_categoria_window.geometry("200x100")

        adicionar_categoria_window.iconbitmap("pizza.ico")

        # Label e campo de entrada para o nome da categoria
        label_nome = tk.Label(adicionar_categoria_window, text="Digite o nome da categoria:")
        label_nome.pack()

        entry_nome = tk.Entry(adicionar_categoria_window)
        entry_nome.pack()

        # Botão personalizado para adicionar a categoria
        # Botão personalizado para editar a categoria
        frame_botoes = tk.Frame(adicionar_categoria_window)
        frame_botoes.pack()

        botao_ok = tk.Button(frame_botoes, text="OK", command=lambda: self.cadastrar_categoria(entry_nome.get(), adicionar_categoria_window))
        botao_ok.pack(side=tk.LEFT)

        botao_cancelar = tk.Button(frame_botoes, text="Cancelar", command=adicionar_categoria_window.destroy)
        botao_cancelar.pack(side=tk.RIGHT)

    def cadastrar_categoria(self, nome_categoria, janela):
        if nome_categoria:
            # Insira a categoria no banco de dados
            conn = criar_conexao()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome_categoria,))
            conn.commit()
            conn.close()

            # Atualize a Treeview para refletir a nova categoria
            self.preencher_treeview()

            # Feche a janela de adicionar categoria
            janela.destroy()

    

    def editar_categoria(self):
        # Obtenha o item selecionado na Treeview
        item_selecionado = self.treeview.selection()

        # Verifique se um item foi selecionado
        if item_selecionado:
            # Obtenha os valores das colunas "ID" e "Nome" do item selecionado
            categoria_id = self.treeview.item(item_selecionado, "values")[0]
            nome_categoria = self.treeview.item(item_selecionado, "values")[1]

            # Crie uma nova janela para editar categoria
            editar_categoria_window = tk.Toplevel(self.root)
            editar_categoria_window.title("Editar Categoria")
            editar_categoria_window.geometry("200x100")

            editar_categoria_window.iconbitmap("pizza.ico")

            # Label e campo de entrada para o nome da categoria
            label_nome = tk.Label(editar_categoria_window, text="Editar o nome da categoria:")
            label_nome.pack()

            entry_nome = tk.Entry(editar_categoria_window)
            entry_nome.insert(0, nome_categoria)  # Preenche o campo com o nome existente
            entry_nome.pack()

            # Botão personalizado para editar a categoria
            frame_botoes = tk.Frame(editar_categoria_window)
            frame_botoes.pack()

            botao_ok = tk.Button(frame_botoes, text="OK", command=lambda: self.salvar_edicao_categoria(categoria_id, entry_nome.get(), editar_categoria_window))
            botao_ok.pack(side=tk.LEFT)

            botao_cancelar = tk.Button(frame_botoes, text="Cancelar", command=editar_categoria_window.destroy)
            botao_cancelar.pack(side=tk.RIGHT)

    def salvar_edicao_categoria(self, categoria_id, novo_nome_categoria, janela):
        if novo_nome_categoria:
            # Atualize a categoria no banco de dados
            conn = criar_conexao()
            cursor = conn.cursor()
            cursor.execute("UPDATE categorias SET nome = ? WHERE id = ?", (novo_nome_categoria, categoria_id))
            conn.commit()
            conn.close()

            # Atualize a Treeview para refletir a categoria editada
            self.preencher_treeview()

            # Feche a janela de editar categoria
            janela.destroy()

    def excluir_categoria(self):
        # Obtenha o item selecionado na Treeview
        item_selecionado = self.treeview.selection()

        # Verifique se um item foi selecionado
        if item_selecionado:
            # Confirme com o usuário antes de excluir a categoria
            confirmacao = tk.messagebox.askokcancel("Confirmar Exclusão", "Tem certeza que deseja excluir esta categoria?")

            if confirmacao:
                # Se o usuário confirmar, obtenha o ID da categoria a ser excluída
                categoria_id = self.treeview.item(item_selecionado, "values")[0]

                # Exclua a categoria do banco de dados
                conn = criar_conexao()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
                conn.commit()
                conn.close()

                # Atualize a Treeview para refletir a categoria excluída
                self.preencher_treeview()

if __name__ == "__main__":
    root = tk.Tk()
    app = CategoriaTela(root)
    root.mainloop()