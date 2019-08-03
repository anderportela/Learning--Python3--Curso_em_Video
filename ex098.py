#Primeira contagem: 1 até 10 de 1 em 1
#Segunda contagem: 10 até 0 de 2 em 2
#Terceira contagem: Valores personalizados
from time import sleep
def count(i, f, p):
    print('*'*50)
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    sleep(1.5)
    print()
    c = i
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        while c <= f:
            print(f'{c} ',end='', flush = True)
            sleep(0.5)
            c += p
        print('Fim!')
    elif i > f:
        c = i
        while c >= f:
            print(f'{c} ', end='', flush = True)
            sleep(0.5)
            c -= p
        print('Fim!')
    print('*'*50)
count(1, 10, 1)
print()
count(10, 0, 2)
print()
print('Personalize uma contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
print()
count(ini, fim, pas)