n1 = float(input('Digite a sua primeira nota: \n'))
n2 = float(input('Digite a sua segunda nota: \n'))
med = (n1+n2)/2
if med < 5:
    print('REPROVADO')
elif 6.9 > med > 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
