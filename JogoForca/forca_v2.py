# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos


import random
from utils import imprimeForca


class Hangman:	

	def __init__(self, word):
		self.word = word
		self.secret_word = []
		self.wrong_letters = []

		
	# Método para adivinhar a letra
	def guess(self, letter):
		for letra in self.word:			
			if letra == letter:
				self.secret_word.append(letter)
				break
		if letter not in self.word:
				self.wrong_letters.append(letter)
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if len(self.wrong_letters) == 7:			
			return True

		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if len(self.word) == len(self.secret_word):
			return True
	

	# Método para não mostrar a letra no board
	def hide_word(self):
		for letra in self.word:
			if letra in self.secret_word:
				print(letra, end='')
			else:
				print('_', end='')
		
		print('\n')
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(imprimeForca.forca[len(self.wrong_letters)])
		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open('JogoForca\BancoPalavras.txt', "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while True:
		game.print_game_status()
		game.hide_word()
		letter = input('Informe uma letra: ')
		if letter == '9':
			break
		game.guess(letter)

		# De acordo com o status, imprime mensagem na tela para o usuário
		if game.hangman_won():
			print ('\nParabéns! Você venceu!!')
			break
		if game.hangman_over():
			print ('\nGame over! Você perdeu.')
			print ('A palavra era ' + game.word)
			break
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')
	

if __name__ == "__main__":
	main()
