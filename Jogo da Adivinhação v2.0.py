from random import randint
print('ESTOU PENSANDO EM UM NÚMERO DE 0 A 10.... TENTE ADVINHAR....')
p = int(input('Em qual número estou pensando? '))
c = 1
r = randint(0,10)
while p is not r:
    c = c + 1
    p = int(input('Tente de novo. Em qual número estou pensando? '))
print('\nParabéns! Você precisou de {} tentativas para acertar o número!'.format(c))
