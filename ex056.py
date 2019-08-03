si = 0
mi = 0
mih = 0
nhv = ''
mai = 0
for c in range(1,5):
    print('******** {}ª Pessoa*******'.format(c))
    n = input('Nome: ').strip()
    i = int(input('Idade: '))
    s = input('Sexo [M/F]:  ').strip()
    si += i
    if c == 1 and s in 'Mm':
        mih = i
        nhv = n
    if s in 'Mm' and i > mih:
        mih = i
        nhv = n
    if s in 'Ff' and i < 21:
        mai = mai + 1
mi = si / 4
print(' \nA média de idade do grupo é de {} anos.'.format(mi))
print('\nO homem mais velho é o : {}'.format(nhv))
if mai > 1:
    print('\nHá {} mulheres com idade abaixo de 21 anos.'.format(mai))
else:
    print('\nHá {} mulher com idade abaixo de 21 anos.'.format(mai))