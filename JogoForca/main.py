from utils import imprimeForca
from random import randint

def sotearPalavra():
    palavra = open('JogoForca\BancoPalavras.txt', 'r')
    lenPalavras = sum(1 for line in palavra)
    numAleatorio = randint(0, lenPalavras)
    palavra.close

    palavra = open('JogoForca\BancoPalavras.txt', 'r')
    for n, line in enumerate(palavra):    
        if numAleatorio == n:
            palavraSorteada = line.lower()
            palavra.close
            break
    
    return palavraSorteada.replace('\n','')
    

def verificarLetra(letraJogador = ''):
    for letra in palavraSorteada:  
        if letraJogador == letra:
            letrasCertas.append(letraJogador)
    if letraJogador not in palavraSorteada:
        letrasErradas.append(letraJogador)    
    

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
    print(imprimeForca.forca[len(letrasErradas)])
    construirPalavra()
    while True:
        letraJogador = input('\nInforme uma letra: ')
        if letraJogador in letrasCertas or letraJogador in letrasErradas:
            print('Letra Repetida! Digite uma letra nova!')
            False
        else:
            break

    #stop teste
    if letraJogador == '9':
        break

    verificarLetra(letraJogador)
    print('\nLetras Certas: ', letrasCertas, end='')
    print('\nLetras Erradas: ', letrasErradas)
    if len(letrasErradas) == 7:
        print('Você perdeu!')
        break

if len(letrasCertas) == len(palavraSorteada):
    print(f'Parabéns! Você acertou a palavra {palavraSorteada}!')
