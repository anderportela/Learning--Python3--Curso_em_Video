pt = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('\nDigite a razão da PA: \n'))
for c in range(pt, pt + (10*r), r):
    print(c, end=' ')
