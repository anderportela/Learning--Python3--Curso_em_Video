def Área():
    print(f'\033[1;34mA área do terreno {l:.2f}m x {c:.2f}m é de {l*c:.2f}m².\033[m')


print(f'\n\033[1;31m{"Qual é a área do terreno?":^100}\033[m')
print()
print('*'*100)
l = float(input('\nDigite a largura do terreno em metros: '))
c = float(input('\nDigite o comprimento do terreno em metros: '))
print()
Área()