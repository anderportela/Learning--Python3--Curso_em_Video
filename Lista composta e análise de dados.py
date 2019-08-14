princ = list()
temp = list()
mai = men = 0
while True:
    temp.append(str(input('\nNome: ')))
    temp.append(float(input('\nMassa: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    c = str(input('\nVocê quer continuar [S/N]? ')).upper()
    if c not in 'SN':
        c = str(input('\nOpçao Inválida! Digite S ou N:'))
    elif c == 'N':
        break
    elif c == 'S':
        continue
print(f'\nForam cadastradas {len(princ)} pessoas')
print(f'\nA maior massa foi de {mai}kg. Que pertence a ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(f'\n\nA menor massa foi de {men}kg. Que pertence a ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')
