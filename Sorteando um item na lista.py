import random
a1 = input('Escreva o nome do primeiro aluno: ')
a2 = input('\nEscreva o nome do segundo aluno: ')
a3 = input('\nEscreva o nome do terceiro aluno: ')
a4 = input('\nEscreva o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
a = random.choice(lista)
print('\nHoje, {} irá apagar o quadro!'.format(a))
