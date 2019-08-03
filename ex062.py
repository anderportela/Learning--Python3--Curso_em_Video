pt = int(input('\nPrimeiro termo:'))
r = int(input('\nRazão da PA: '))
t = pt
c =1
total = 0
te = 10
while te > 0:
    total += te
    while c <= total:
        print('{} '.format(t), end='')
        c += 1
        t += r
    te = int(input('\n\nQuantos termos você quer adicionar na PA? '))
print('\nForam exibidos {} termos dessa PA!'.format(total))


