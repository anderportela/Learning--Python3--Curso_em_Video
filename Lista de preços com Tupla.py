lista = ('PS4 Slim 1TB', 1729.90, 'Xbox One S 1TB', 1129.90, 'Nintendo Switch', 1659.90)
print('\n***************************\033[31mLISTA DE PREÇOS\033[m******************************')
print('\n')
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R$ {lista[item]:.2f}')
print('\n*************************************************************************')
