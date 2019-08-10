d = float(input('Digite a distância da viagem em km/h: '))
if d > 200:
    vl = 0.45 * d
    print('A sua viagem custa R${:.2f}'.format(vl))
else:
    vc = 0.5 * d
    print('A sua viagem custa R${:.2f}'.format(vc))
