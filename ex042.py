r1 = int(input('Digite um segmento de reta em cm: '))
r2 = int(input('Digite outro segmento de reta em cm: '))
r3 = int(input('Digite outro segmento de reta em cm: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os seguimentos acima podem formar um triângulo ', end='')
    if r1 == r2 ==r3:
        print('equilátero!')
    elif r1 != r2 != r3 != r1:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('Não é possível formar um triângulo com os segmentos acima!')