# users = {1: 'Hans', 2: 'Elonore', 3: 'Adam'}

# for key, value in users.items():
# 	print(key, value)

from random import shuffle
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)
print(nomes)
