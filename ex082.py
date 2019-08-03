geral = []
pares = []
impares = []
while True:
    v = int(input('\nDigite um valor inteiro: '))
    geral.append(v)
    r = str(input('\nQuer continuar? [S/N]: ')).upper()
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    if r == 'N':
        break
    elif r == 'S':
        continue
    else:
        r = str(input('\nOpção Inválida! Digite N ou S: ')).upper()
        if r == 'N':
            break
print(f'\nA lista completa dos valores digitados é: {geral}')
print(f'\nOs números pares digitados foram: {pares}')
print(f'\nOs números ímpares digitados foram: {impares}')