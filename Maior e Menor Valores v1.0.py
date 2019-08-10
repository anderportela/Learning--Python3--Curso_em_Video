n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n3))
else:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n3))
if n1 < n2:
    if n1 < n3:
        print('E o menor número é {}'.format(n1))
    else:
        print('E o menor número é {}'.format(n3))
else:
    if n2 < n3:
        print('E o menor número é {}'.format(n2))
    else:
        print('E o menor número é {}'.format(n3))
