from operator import le
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
    print('Palavra: ', end='')
    for letra in palavraSorteada:
        if letraJogador == letra:
            print(letraJogador, end='')
            letrasCertas.append(letraJogador)
        elif letra == ' ':
            print(letra, end='')
        else:
            for i in letrasCertas:
                if i == letraJogador:
                    print(i, end='')
                else:
                    print(letra.replace(letra, '_'), end='')
    
    if letraJogador not in palavraSorteada:
        letrasErradas.append(letraJogador)


letrasCertas = []
letrasErradas = []

palavraSorteada = sotearPalavra()
verificarLetra()

while len(letrasCertas) < len(palavraSorteada):    
    letraJogador = input('\nInforme uma letra: ')
    verificarLetra(letraJogador)
    print('\nLetras Certas: ', letrasCertas, end='')
    print('\nLetras Erradas: ', letrasErradas)
    if len(letrasErradas) == 5:
        break
    

    #stop teste
    if letraJogador == '9':
        break
