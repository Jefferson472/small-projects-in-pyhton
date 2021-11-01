from tkinter import *
from tkinter import ttk

class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('Tela de Cadastro')
        self.root.geometry('575x300')
        self.root.resizable(False, False)

        self.tree = ttk.Treeview()
        s = ttk.Style()
        s.theme_use('clam')
        self.tree = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4"), show='headings', height=7)



def main():
    janela = Interface()
    janela.root.mainloop()

if __name__ == '__main__':
    main()