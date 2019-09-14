from time import sleep
from random import randint

#Definindo funções:

def sorteia(num):
    print('\nSorteando 5 valores aleatórios de 1 a 10...')
    print()
    for c in range(0, 5):
        n = randint(1, 10)
        num.append(n)
        print(f'\033[1;33m{n}\033[m ', end = '', flush = True)
        sleep(0.5)

def somaPar(par):
    soma = 0
    for p in par:
        if p %2 == 0:
            soma += p
    print(f'\n\nA soma dos valores pares da lista \033[1;33m{numeros}\033[m é \033[1;31m{soma}\033[m')

#Programa principal:

numeros = list()
soma = 0
sorteia(numeros)
somaPar(numeros)
