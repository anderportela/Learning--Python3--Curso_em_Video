a = int(input('Digite um ano: '))
if a % 4:
    if a % 100:
        print('{} não é um ano bissexto!'.format(a))
    else:
        print('{} é um ano bissexto!')
else:
    if a % 400:
        print('{} é um ano bissexto!'.format(a))
    else:
        print('{} não é um ano bissexto!'.format(a))
