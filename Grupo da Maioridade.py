ma = 0
me = 0
for c in range(1, 8, 1):
    an = int(input('Digite seu ano de nascimento: '))
    id = 2018 - an
    if id >= 21:
        ma = ma + 1
    else:
        me = me + 1
print('\nHá {} pessoas que já atingiram a maioridade'.format(ma))
print('\nHá {} pessoas que ainda não atingiram a maioridade'.format(me))
