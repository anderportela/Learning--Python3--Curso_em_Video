lista = []
c = 0
while True:
    v = int(input('\nDigite um valor: '))
    lista.append(v)
    c += 1
    r = str(input('\nQuer continuar? [S/N]? ')).upper()
    if r == 'N':
        break
    elif r == 'S':
        continue
    else:
        r = str(input('\nOpção Inválida! Digite S ou N: ')).upper()
        if r == 'N':
            break
if c == 1:
    print('\nFoi digitado 1 valor!')
else:
    print(f'\nForam digitados {c} valores!')
lista.sort(reverse = True)
print(f'\nOs valores digitados em ordem decrescente: {lista}')
if 5 in lista:
    print('\nO valor 5 foi digitado!')
else:
    print('\nO valor 5 não foi digitado!')