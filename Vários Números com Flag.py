c = s = 0
while True:
    n = int(input('\nDigite um número inteiro (999 para cancelar): '))
    if n == 999:
        break
    c += 1
    s += n
if c == 1:
    print(f'\nFoi digitado {c} número e a soma foi {s}')
elif c == 0:
    print(f'\nNão foram computados valores, pois você digitou o comando para \033[4;31mcancelar\033[m antes dos valores válidos!')
else:
    print(f'\nForam digitados {c} números e a soma foi {s}')



