lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para {cont + 1}ª posição: ')))
ma = me = lista[0]
print(f'\nForam digitados os valoes: {lista}')
for v in lista:
    if v > ma:
        ma = v
    if v < me:
        me = v
print(f'\nO maior valor é: {ma}', end='')
for p, c in enumerate(lista):
    if c == ma:
        print(f' na {p + 1}ª posição')
print(f'\nO menor valor é: {me}', end='')
for p, c in enumerate(lista):
    if c == me:
        print(f' na {p + 1}ª posição')
