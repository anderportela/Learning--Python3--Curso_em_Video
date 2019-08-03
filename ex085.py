num = [[], []]
c = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    c += 1
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'\nOs números pares digitados foram: {num[0]}')
print(f'\nOs números ímpares digitados foram: {num[1]}')