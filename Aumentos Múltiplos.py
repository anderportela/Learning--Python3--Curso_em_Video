s = float(input('Digite seu salário em R$: '))
if s > 1250:
    a1 = s*1.1
    print('Seu novo salário será R${:.2f}'.format(a1))
else:
    a2 = s*1.15
    print('Seu novo salário será R${:.2f}'.format(a2))
