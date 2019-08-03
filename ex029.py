v = int(input('Velocidade do veículo em km/h: '))
m = 0
if v > 80:
    mt = (v-80)*7
    print ('Você foi multado(a) em R${} por exceder o limite de velocidade!'.format(mt))