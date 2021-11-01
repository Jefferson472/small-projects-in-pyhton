class JogoDaVelha:

    def __init__(self):
        self.jogadaX = 0
        self.jogadaY = 0


    def desenharBoard(self):
        for i in range(0, 3):    
            for j in range(0, 3):                
                if self.jogadaX == i and self.jogadaY == j:
                    print('[X]', end='') 
                else:        
                    print('[ ]', end='')
            print()
        

    def jogaPlayer(self):
        self.jogadaX = int(input('Informe a coordenada x: '))
        self.jogadaY = int(input('Informe a coordenada y: '))     
        

    def jogaIA(self):
        pass


    def verficaStatus(self):
        pass


def main():
    velha = JogoDaVelha()
    velha.desenharBoard()
    velha.jogaPlayer()    

    velha.desenharBoard()



if __name__ == "__main__":
    main()