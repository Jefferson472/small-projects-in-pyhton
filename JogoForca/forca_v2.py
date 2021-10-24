# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos


import random
from utils import imprimeForca


class Hangman:
	
	def __init__(self, word):
		pass

		
	# Método para adivinhar a letra
	def guess(self, letter):
		pass
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		pass
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		pass

	# Método para não mostrar a letra no board
	def hide_word(self):
		pass
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(imprimeForca.forca[len(letrasErradas)])
		pass

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("BancoPalavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while len(letrasCertas) < len(game):    
		Hangman.print_game_status()
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
			print(f'Você perdeu! A palavra era {palavraSorteada}')
			break

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

		
if __name__ == "__main__":
	main()
