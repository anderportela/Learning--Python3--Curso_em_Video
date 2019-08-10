tg = mil = ct = ctp = 0
print('\n                   \033[1;36mVAMOS FAZER COMPRAS?\033[m')
while True:
    print('---------------------------------------------------------------------')
    p = str(input('\nDigite o nome do produto: ')).capitalize()
    ct += 1
    if ct == 1:
        mb = p
    else:
        if p < mb:
            mb = p
    pr = float(input('\nDigite o preço do produto: '))
    ctp += 1
    if ctp == 1:
        pmb = pr
    else:
        if pr < pmb:
            pmb = pr
    tg += pr
    if pr > 1000:
        mil += 1
    c = str(input('\nQuer continuar as compras? [S/N]: ')).upper()
    if c not in 'SN':
        c = str(input('\nQuer continuar as compras? [S/N]: ')).upper()
    if c == 'N':
        break
print('-----------------------------------------------------------------')
print(f'\nO total gasto nas compras foi de \033[1;33mR$ {tg:.2f}\033[m')
print(f'\nForam comprados \033[1;31m{mil}\033[m produto(s) com valor acima de R$ 1000.00.')
print(f'\nO produto mais barato da compra é \033[1;4;32m{mb}\033[m e custou \033[1;32mR$ {pmb:.2f}\033[m')
