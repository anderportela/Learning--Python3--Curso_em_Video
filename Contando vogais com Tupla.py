nomes = ('Antonio', 'Fatima', 'Anderson', 'Juliana')
print('*'*60)
print('                \033[32mQUAIS SÃO AS  VOGAIS?\033[m                       ')
print('*'*60)
for nome in nomes:
    print(f'\n\nNa palavra {nome} temos: ', end='')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print('\033[31m',end='')
            print(letra.upper(), end='')
            print(' ',end='')
            print('\033[m', end='')
print('\n')
