import math
a = float(input('Digite o valor de um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(' O seno do âgulo é {:.2f}\n O cosseno é {:.2f}\n A tangente é {:.2f}'.format(s, c, t))
