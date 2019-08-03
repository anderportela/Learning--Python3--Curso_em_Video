valores = []
while True:
    n = int(input('\nDigite um valor inédito: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        n = int(input('\nValor repetido! Digite um valor inédito: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    if r == 'N':
        break
    elif r == 'S':
        continue
    else:
        r = str(input('Opção Inválida! Digite N ou S: ')).upper()
        if r == 'N':
            break
valores.sort()
print(f'\nOs valores digitados foram: \033[31m{valores}\033[m')