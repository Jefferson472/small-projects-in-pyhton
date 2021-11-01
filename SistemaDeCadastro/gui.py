from abc import abstractproperty
from tkinter import *
from tkinter import ttk
from _Cadastro import Cadastro


root = Tk()


def gravar():    
    produto = produtoInput.get()
    quantidade = qntdInput.get()
    valor = valorInput.get()
    cadastroDB.addProduto(produto, quantidade, valor)

def buscaProduto():
    produto = produtoInput.get()
    if produto == '':
        listar(cadastroDB.listarProdutos())
    else:
        listar(cadastroDB.buscaProduto(produto))


def deletarProduto():
    
    pass

def listar(lista_Produtos):
    s = ttk.Style()
    s.theme_use('clam')

    # Add a Treeview widget
    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings', height=7)

    tree.column("# 1", anchor=CENTER, width=50)
    tree.heading("# 1", text="ID")
    tree.column("# 2", anchor=CENTER, width=300)
    tree.heading("# 2", text="Produto")
    tree.column("# 3", anchor=CENTER, width=100) 
    tree.heading("# 3", text="Quantidade")
    tree.column("# 4", anchor=CENTER, width=100)
    tree.heading("# 4", text="Valor")

    for i in lista_Produtos:
        tree.insert("", 'end', values=(i[0], i[1], i[2], i[3]))
    

    tree.grid(row=2, columnspan=10, pady=10)    
    

root.title('Tela de Cadastro')
root.geometry('575x300')
root.resizable(False, False)

produtoLabel = Label(text='Produto: ')
produtoLabel.grid(row=0, column=0)
produtoInput = Entry(root, bd=5, relief='flat', highlightthickness=1)
produtoInput.grid(row=0, column=1, padx=10, pady=10)

qntdLabel = Label(text='Quantidade: ')
qntdLabel.grid(row=0, column=2)
qntdInput = Entry(root, bd=5, relief='flat', highlightthickness=1)
qntdInput.grid(row=0, column=4, padx=10)

valorLabel = Label(text='Valor: ')
valorLabel.grid(row=0, column=5)
valorInput = Entry(root, width=10, bd=5, relief='flat', highlightthickness=1)    
valorInput.grid(row=0, column=6, padx=10)

buttonFrame = Frame(root)
buttonFrame.grid(columnspan=10, pady=10)

btnGravar = Button(buttonFrame, text='Gravar', command=gravar)
btnGravar.grid(row=0, column=0, pady=10, padx=10)

btnPesquisar = Button(buttonFrame, text='Pesquisar', command=buscaProduto)
btnPesquisar.grid(row=0, column=1, pady=10, padx=10)

btnExcluir = Button(buttonFrame, text='Excluir')
btnExcluir.grid(row=0, column=2, pady=10, padx=10)

cadastroDB = Cadastro('Cadastro.db')


listar(cadastroDB.listarProdutos())



root.mainloop()

cadastroDB.fechaConexao()
