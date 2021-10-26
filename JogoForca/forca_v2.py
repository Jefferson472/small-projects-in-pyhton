# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos


import random
from utils import imprimeForca
secret_word = []
wrong_letters = []

class Hangman:	

	def __init__(self, word):
		self.word = word

		
	# Método para adivinhar a letra
	def guess(self, letter, word):
		for letra in word:			
			if letra == letter:
				secret_word.append(letter)
				break
		if letter not in word:
				wrong_letters.append(letter)
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self, word):
		if len(wrong_letters) == 7:
			return True

		
	# Método para verificar se o jogador venceu
	def hangman_won(self, word):
		if len(word) == len(secret_word):
			return True
	

	# Método para não mostrar a letra no board
	def hide_word(self, word):
		for letra in word:
			if letra in secret_word:
				print(letra, end='')
			else:
				print('_', end='')

		print('\n')
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(imprimeForca.forca[len(wrong_letters)])
		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("BancoPalavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while True:
		game.print_game_status()
		game.hide_word(game.word)
		letter = input('Informe uma letra: ')
		if letter == '9':
			break
		game.guess(letter, game.word)

		# De acordo com o status, imprime mensagem na tela para o usuário
		if game.hangman_won(game.word):
			print ('\nParabéns! Você venceu!!')
			break
		if game.hangman_over(game.word):
			print ('\nGame over! Você perdeu.')
			print ('A palavra era ' + game.word)
			break
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')


if __name__ == "__main__":
	main()
