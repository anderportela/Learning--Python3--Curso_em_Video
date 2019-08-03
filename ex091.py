from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
ranking = ()
c = 0
print('*'*100)
print(f'\033[31m{"VOCÊ TEM DADO EM CASA? (oo)":^100}\033[m')
print('*'*100)
print(f'\033[32m{"VALORES SORTEADOS":^100}\033[m')
print()
for k, v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking= sorted(dados.items(), key=itemgetter(1), reverse=True)
print()
sleep(1)
print('*'*100)
print(f'\033[34m{"RANKING":^100}\033[m')
sleep(2)
print()
for k, v in ranking:
    print(f'Em {c+1}º ficou {k} porque tirou {v} no dado')
    c += 1
    sleep(1)