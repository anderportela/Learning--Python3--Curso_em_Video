num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
a = int(input('\nDigite um número de 0 a 20: '))
while a > 20:
    a = int(input('\nTente novamente. Digite um número entre 0 e 20: '))
    if a in range(0, 21):
        break
    else:
        a = int(input('\nTente novamente. Digite um número entre 0 e 20: '))
print(f'\nVocê digitou o número \033[33m{num[a]}\033[m')
