from time import sleep
from random import randint
lj = list()
jogo = list()
print('*'*60)
print('                        MEGA SENA')
print('*'*60)
qj = int(input('Quantos jogos você quer fazer? '))
t = 1
while t <= qj:
    c = 0
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            c += 1
        if c >= 6:
            break
    jogo.sort()
    lj.append(jogo[:])
    jogo.clear()
    t += 1
print('*'*60)
print(f'SORTEANDO {qj} JOGOS...')
print('.'*80)
for i, l in enumerate(lj):
    print(f'Jogo {i + 1}: {l}')
    sleep(2)
print('\n*********BOA SORTE************')