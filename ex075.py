n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('\nDigite o segundo número: '))
n3 = int(input('\nDigite o terceiro número: '))
n4 = int(input('\nDigite o quarto número: '))
t1 = (n1, n2, n3, n4)
pares = 0
print(f'\nVocê digitou os seguintes valores: {t1}')
if t1.count(9) == 0:
    print('\nO número 9 não foi digitado! ')
elif t1.count(9) == 1:
    print(f'\n O número 9 foi digitado {t1.count(9)} vez!')
else:
    print(f'\nO número 9 foi digitado {t1.count(9)} vezes!')
if t1.count(3) == 0:
    print('\nO número 3 não foi digitado!')
else:
    print(f'\nO número 3 está na {t1.index(3) + 1}ª posição!')
print(f'\nOs números pares digitados foram: ', end='')
for n in t1:
    if n % 2 == 0:
        print(n, end=' ')