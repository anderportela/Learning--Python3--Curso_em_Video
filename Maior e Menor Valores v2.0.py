op = 'S'
q = m = s = ma = me = 0
while op == 'S':
    n = int(input('\nDigite um número inteiro: '))
    s += n
    q += 1
    if q == 1:
        ma = me = n
    elif n > ma:
        ma = n
    elif n < me:
        me = n
    op = input('\nVocê quer continuar [S/N] ? ').upper().strip()[0]
m = s / q
print('\nForam digitados {} valores'.format(q))
print('\nA média dos valores é {:.2f}'.format(m))
print('\nO maior valor é {} e o menor valor é {}'.format(ma, me))
