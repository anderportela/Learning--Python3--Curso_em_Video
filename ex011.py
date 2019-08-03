a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
print('\nA área da parede é: {:.2f}m²\nSerá necessário {:.2f}l de tinta para pintá-la!'.format(a*l, (a*l)/2))