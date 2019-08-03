soma = 0
for cont in range(1, 501, 2):
    if cont %3 == 0:
        soma = soma + cont
print('A soma dos valores é: {}'.format(soma))
