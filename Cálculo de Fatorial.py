n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro:\n'))
op = 0
while op != 5:
    op = int(input('Digite uma opçao abaixo: \n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Outros valores\n[5] Encerrar\n'))
    if op == 1:
        print('A soma dos números {} e {} é {} !\n'.format(n1, n2, n1+n2))
    elif op == 2:
        print('A multiplicação entre {} e {} é {} !\n'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('O maior número é {} !\n'.format(n1))
        elif n2 > n1:
            print('O maior número é {} !\n'.format(n2))
        else:
            print('Os números são iguais!\n')
    elif op == 4:
        print('Informe os novos valores:\n')
        n1 = int(input('Digite um valor inteiro: '))
        n2 = int(input('Digite outro valor inteiro:\n'))
print('Finalizando....')
