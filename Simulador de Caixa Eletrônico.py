c1 = c10 = c20 = c50 = 0
print('\n---------BANCO ABUTRE$-----------')
print('\nTrabalhamos com notas de R$1, R$10, R$20 e R$50!')
print('\n*******************************************************')
s = int(input('\nQual valor você deseja sacar? '))
while True:
    while (s / 50) >= 1:
        c50 += 1
        s = s - 50
    if s < 50:
        while (s / 20) >= 1:
            c20 += 1
            s = s - 20
        if s < 20:
            while (s / 10) >= 1:
                c10 += 1
                s = s - 10
            if s < 10:
                while (s / 1) >= 1:
                    c1 += 1
                    s = s -1
                if s < 1:
                    break
print(f'\nForam sacadas {c50} cédula(s) de R$50.00')
print(f'Foram sacadas {c20} cédula(s) de R$20.00')
print(f'Foram sacadas {c10} cédula(s) de R$10.00')
print(f'Foram sacadas {c1} cédula(s) de R$ 1.00')
print('\n*****************************************************')
