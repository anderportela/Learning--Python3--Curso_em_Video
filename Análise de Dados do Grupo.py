p18 = h = m20 = 0
while True:
    print('\n----------CADASTRO DE PESSOAS----------------')
    i = int(input('\nDigite a idade: '))
    if i > 18:
        p18 += 1
    s = str(input('\nDigite o sexo [M/F]: ')).upper()
    if s == 'M':
        h += 1
    if i > 20 and s == 'F':
        m20 += 1
    if s not in 'MF':
        s = str(input('\nDigite o sexo: [M/F]: ')).upper()
    p = str(input('\nVocê quer continuar? [S/N]: ')).upper()
    if p not in 'SN':
        p = str(input('\nVocê quer continuar? [S/N]: ')).upper()
    if p == 'N':
        break
print(f'\nForam cadastrados {h} homens. ')
print(f'\nForam cadastradas {p18} pessoas maiores de 18 anos.')
print(f'\nForam cadastradas {m20} mulheres acima de 20 anos.')
print('-------------------------------------------------------')
