from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = sqrt(co**2 + ca**2)
print('O comprimento da hipotenusa desse triângulo é: {}'.format(hip))
