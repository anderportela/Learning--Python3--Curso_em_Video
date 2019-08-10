from random import randint
print('ESTOU PENSANDO EM UM NÚMERO DE 0 A 5... TENTE ADVINHAR...')
n = int(input('Em qual número eu pensei? '))
c = randint(0, 5)
if n == c:
    print('Parabéns! Pensei no {} e você advinhou!'.format(c))
else:
    print('Não foi dessa vez... Você digitou {} e pensei no {}'.format(n, c))
