f = input('Digite uma frase: \n').strip().upper()
sep = f.split()
j = ''.join(sep)
inv = ''
for l in range(len(j) -1 , -1, -1):
    inv += j[l]
if inv == j:
    print('A frase {} é um palíndromo!'.format(f))
else:
    print('A frase {} não é um palíndromo!'.format(f))