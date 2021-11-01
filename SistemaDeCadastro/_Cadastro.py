import sqlite3


class Cadastro():
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos
        (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, quantidade INTEGER)
            ''')
        print("Conexão aberta com sucesso!")
        
    
    def fechaConexao(self):
        self.conn.close()
        print("Conexão fechada com sucesso!")        
    

    def salvaAlteracoes(self, nome, acao):
        self.conn.commit()
        print(f'Produto {nome} {acao} com sucesso!')      


    def alteraProduto(self, preco=0, quantidade=0, nome=''):
        self.cursor.execute("""UPDATE produtos SET preco = ?, quantidade = ? WHERE nome = ?""", (
            preco, quantidade, nome))
        self.salvaAlteracoes(nome, 'alterado')     
            

    def addProduto(self, nome, preco, quantidade):
        self.cursor.execute("""INSERT INTO produtos VALUES (NULL, ?, ?, ?)""", (
            nome, preco, quantidade))
        self.salvaAlteracoes(nome, 'adicionado')      


    def buscaProduto(self, nome):
        self.cursor.execute("""SELECT * FROM produtos WHERE nome = ? """, (nome,))
        return self.cursor.fetchall()


    def listarProdutos(self):
        self.cursor.execute("""SELECT * FROM produtos""")
        return self.cursor.fetchall()
    

    def excluiProduto(self, nome):
        self.cursor.execute("""DELETE FROM produtos WHERE nome = ?""", (nome,))
        self.salvaAlteracoes(nome, 'excluído')


# def main():



# if __name__ == "__main__":
#     main()