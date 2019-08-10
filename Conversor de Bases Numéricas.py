num = int(input('Digite um valor inteiro decimal: '))
opc = int(input('\nDigite 1 para converter em binário:  \nDigite 2 para octal:  \nDigite 3 para hexadecimal: \n'))
if opc == 1:
    print(' O número {} em binário é: {}'.format(num, bin(num)))
elif opc == 2:
    print('O número {} em octal é: {}'.format(num, oct(num)))
elif opc == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)))
else:
    print('Opção Inválida. Tente novamente!')
