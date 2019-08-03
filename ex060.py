'''**********************************MÉTODO WHILE***********************************'''

n = int(input('Digite um valor inteiro: '))
c = n
f = 1
print('{} ! = '.format(n), end = '')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))

'''**********************************MÉTODO FOR******************************************

n = int(input('Digite um valor inteiro: '))
c = n
f = 1
print('{} ! = '.format(n), end = '')
for c in range(n, 0, -1):
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
print('{}'.format(f))'''