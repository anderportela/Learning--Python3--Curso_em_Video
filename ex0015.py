k = float(input('Quantos km o carro percorreu? '))
d = int(input('Por quantos dias o carro ficou alugado? '))
p = (k*0.15)+(d*60)
print('O valor total a ser pago é de R${:.2f} '.format(p))