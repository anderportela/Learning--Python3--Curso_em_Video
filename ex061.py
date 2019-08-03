pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('\nDigite a razão da PA: '))
t = pt
c = 1
print('\nOs dez primeiros termos da PA são: \n')
while c <= 10:
    print('{} '.format(t), end='')
    t += r
    c += 1
print('\n')