#Definido funções:
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\n\033[1;31mVocê não digitou um número inteiro!\033[m\n')
        if ok:
            break
    return valor

#Programa principal:
print('-*-'*15)
num = leiaInt('Digite um número inteiro: ')
print(f'\nVocê digitou o número \033[1;32m{num}\033[m')
