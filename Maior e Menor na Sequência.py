ma = 0
me = 0
for p in range(1, 6, 1):
    pe = float(input('Peso da {}ª pessoa em kg: '.format(p)))
    if p == 1:
        ma = pe
        me = pe
    else:
        if pe > ma:
            ma = pe
        if pe < me:
            me = pe
print('\nO maior peso é: {}kg'.format(ma))
print('\nO menor peso é: {}kg'.format(me))
