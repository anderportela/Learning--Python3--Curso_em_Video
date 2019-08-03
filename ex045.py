import random
print('\033[1;33mDESAFIO DO JOKENPO!!!!!!\n')
print('\033[034mDigite 1 para Pedra')
print('Digite 2 para Papel ')
print('Digite 3 para Tesoura\033[m')
cpu = random.randint(1,3)
play = int(input())
if play == 1 and cpu == 1:
    print('Empate!!')
elif play == 1 and cpu == 2:
    print('Você perdeu!!')
elif play == 1 and cpu == 3:
    print('Você ganhou!!')
elif play == 2 and cpu == 1:
    print('Você ganhou!!')
elif play == 2 and cpu == 2:
    print('Empate!!')
elif play == 2 and cpu == 3:
    print('Você perdeu!!')
elif play == 3 and cpu == 1:
    print('Você perdeu!!')
elif play == 3 and cpu == 2:
    print('Você ganhou!!')
elif play == 3 and cpu == 3:
    print('Empate!!')
else:
    print('Opção Inválida!!')