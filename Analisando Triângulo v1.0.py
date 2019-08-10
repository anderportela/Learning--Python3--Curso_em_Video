r1 = int(input('Digite um segmento de reta em cm: '))
r2 = int(input('Digite outro segmento de reta em cm: '))
r3 = int(input('Digite outro segmento de reta em cm: '))
if(r1 - r2) < r3 < (r1 + r2):
    if(r2 - r3) < r1 < (r2 + r3):
        if(r3 - r1) < r2 < (r3 + r1):
            print('É possível um triângulo com essas retas!')
        else:
            print('Não é possível um triângulo com essas retas!')
    else:
        print('Não é possível um triângulo com essas retas!')
else:
    print('Não é possível um triângulo com essas retas!')
