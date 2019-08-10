data = int(input('Digite a data de nascimento do atleta: \n'))
idade = 2019 - data
if idade <= 9:
    print('Atleta categoria Mirim')
elif 14 > idade > 9:
    print('Atleta categoria Infantil')
elif 19 >= idade > 14:
    print('Atleta categoria Júnior')
elif 20 >= idade > 19:
    print('Atleta categoria Sênior')
else:
    print('Atleta categoria Master')
