soma = 0
for cont in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(cont)))
    if n %2 == 0:
        soma += n
print('A soma dos valores é: {}'.format(soma))
