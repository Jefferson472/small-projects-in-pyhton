from JogoForca.utils import imprimeForca
from random import randint

def sotearPalavra():
    palavra = open('JogoForca\BancoPalavras.txt', 'r')
    lenPalavras = sum(1 for line in palavra)
    numAleatorio = randint(0, lenPalavras)
    palavra.close

    palavra = open('JogoForca\BancoPalavras.txt', 'r')
    for n, line in enumerate(palavra):    
        if numAleatorio == n:
            palavraSorteada = line
            palavra.close
            break
    
    return palavraSorteada.replace('\n','')


def verificarLetra(letraJogador = ''):
    if letraJogador in palavraSorteada:
        letrasCertas.append(letraJogador)
    else:
        letrasErradas.append(letraJogador)

    imprimeForca.forca[len(letrasErradas)]
    

def construirPalavra():
    print('Palavra: ')
    for letra in palavraSorteada:               
        if letra in letrasCertas:
            print(letra, end='')
        else:
            print('_', end='')


letrasCertas = []
letrasErradas = []

palavraSorteada = sotearPalavra()

while len(letrasCertas) < len(palavraSorteada):    
    construirPalavra()
    letraJogador = input('\nInforme uma letra: ')

    #stop teste
    if letraJogador == '9':
        break

    verificarLetra(letraJogador)
    print('\nLetras Certas: ', letrasCertas, end='')
    print('\nLetras Erradas: ', letrasErradas)
    if len(letrasErradas) == 5:
        break



