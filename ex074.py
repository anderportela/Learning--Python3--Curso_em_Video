from random import randint
n1 = randint(0, 9)
n2 = randint(0, 9)
n3 = randint(0, 9)
n4 = randint(0, 9)
n5 = randint(0, 9)
t = (n1, n2, n3, n4, n5)
maior = t[0]
menor = t[0]
if t[1] > maior:
    maior = t[1]
elif t[2] > maior:
    maior = t[2]
elif t[3] > maior:
    maior = t[3]
elif t[4] > maior:
    maior = t[4]
if t[1] < menor:
    menor = t[1]
elif t[2] < menor:
    menor = t[2]
elif t[3] < menor:
    menor = t[3]
elif menor < t[4]:
    menor = t[4]
print('\n')
print(t)
print(f'\nO maior número da tupla é: \033[31m{maior}\033[m')
print(f'\nO menor número da tupla é: \033[34m{menor}\033[m')