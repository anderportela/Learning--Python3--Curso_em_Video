peso = float(input('Digite seu peso em Kg: \n'))
alt = float(input('Digite sua altura em metros: \n'))
imc = peso/(alt*alt )
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif 25 > imc > 18.5:
    print('Você está no peso ideal!')
elif 30 > imc > 25:
    print('Você está com sobrepeso!')
elif 40 > imc > 30:
    print('Você está obeso!')
else:
    print('Você está com obesidade mórbida!')
