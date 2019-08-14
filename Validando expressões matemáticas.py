par = []
e = input('\nDigite uma expressão: ')
for s in e:
    if s == '(':
        par.append('(')
    elif s == ')':
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')
            break
if len(par) == 0:
    print('\nA expreesão é válida !')
else:
    print('\nA expressão não é válida !')
