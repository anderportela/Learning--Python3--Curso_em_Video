from random import randint
v = 0
print('\n------ VAMOS BRINCAR DE PAR OU ÍMPAR! ---------')
while True:
    n = int(input('\nDigite um valor: '))
    poui = str(input('Par ou ímpar? [P/I]: ')).upper()
    r = randint(0, 9)
    if (n + r)% 2 == 0 and poui in 'P':
        print(f'\nVocê ganhou! Você jogou \033[1;35m{n}\033[m e o computador jogou \033[1;31m{r}\033[m. Total \033[1;33m{n + r}\033[m é par!')
    elif (n + r)% 2 == 1 and poui in 'I':
        print(f'\nVocê ganhou! Você jogou \033[1;35m{n}\033[m e o computador jogou \033[1;31m{r}\033[m. Total \033[1;33m{n + r}\033[m é ímpar!')
    else:
        break
    v += 1
print('\n---------GAME OVER----------')
print(f'\nVocê obteve \033[1;33m{v}\033[m vitórias consecutivas!')