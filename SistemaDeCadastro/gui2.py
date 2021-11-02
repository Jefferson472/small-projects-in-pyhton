from tkinter import *
from tkinter import ttk
from _Cadastro import Cadastro

class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('Tela de Cadastro')
        self.root.geometry('575x300')
        self.root.resizable(False, False)

        self.buttonFrame = Frame(self.root)
        self.buttonFrame.grid(columnspan=10, pady=10, row=1)

        self.tree = ttk.Treeview()
        s = ttk.Style()
        s.theme_use('clam')
        self.tree = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4"), show='headings', height=7)
        self.tree.grid(row=2, columnspan=10, pady=10)

        self.tree.column("# 1", anchor=CENTER, width=50)
        self.tree.heading("# 1", text="ID")
        self.tree.column("# 2", anchor=CENTER, width=300)
        self.tree.heading("# 2", text="Produto")
        self.tree.column("# 3", anchor=CENTER, width=100) 
        self.tree.heading("# 3", text="Quantidade")
        self.tree.column("# 4", anchor=CENTER, width=100)
        self.tree.heading("# 4", text="Valor")


    def labelCreator(self,variavel, text, row, column):
        self.variavel = Label(text=(text))
        self.variavel.grid(row=row, column=column)
       

    def inputCreator(self, variavel, row, column, largura=20):
        self.inputVariavel = Entry(self.root, bd=5, relief='flat', highlightthickness=1, width=largura)
        self.inputVariavel.grid(row=row, column=column, padx=10, pady=10)
        print(self.variavel)


    def buttonCreator(self, variavel, text, row, column, comando):
        self.variavel = Button(self.buttonFrame, text=text, command=comando)
        self.variavel.grid(row=row, column=column, padx=10, pady=10)        
        

    def attListaProdutos(self, lista_Produtos):
        for i in lista_Produtos:
            self.tree.insert("", 'end', values=(i[0], i[1], i[2], i[3]))


    def gravar(self):    
        print('Teste')
        self.produto = self.inputVariavel.get()
        print(self.produto)
        self.quantidade = self.inputVariavel.get()
        print(self.quantidade)
        self.valor = self.inputVariavel.get()
        print(self.valor)
        self.cadastroDB.addProduto(self.produto, self.quantidade, self.valor)

    def pesquisar():
        produto = produtoInput.get()
        if produto == '':
            listar(cadastroDB.listarProdutos())
        else:
            listar(cadastroDB.buscaProduto(produto))

    def excluir():        
        pass
        

def main():
    janela = Interface()       
    janela.labelCreator(variavel='ProdutoLabel', text='Produto: ', row=0, column=0)
    janela.inputCreator(variavel='ProdutoInput', row=0, column=1)
    janela.labelCreator(variavel='QntdLabel', text='Quantidade: ', row=0, column=2)
    janela.inputCreator(variavel='QntdInput', row=0, column=3)
    janela.labelCreator(variavel='ValorLabel', text='Valor: ', row=0, column=4)
    janela.inputCreator(variavel='ValorInput', row=0, column=5, largura=10)

    janela.buttonCreator(variavel='btnGravar', text='Gravar', row=0, column=0, comando=janela.gravar)
    janela.buttonCreator(variavel='btnPesquisar', text='Pesquisar', row=0, column=1, comando='pesquisar')
    janela.buttonCreator(variavel='btnExcluir', text='Excluir', row=0, column=2, comando='excluir')
    
    cadastroDB = Cadastro('Cadastro.db')
    janela.attListaProdutos(cadastroDB.listarProdutos())
    janela.root.mainloop()
    cadastroDB.fechaConexao()


if __name__ == '__main__':
    main()