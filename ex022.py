nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em maiusculas: {}'.format(nome.upper()))
print('Nome em minusculas: {}'.format(nome.lower()))
print('O nome tem {} letras!'.format(len(nome)-nome.count(' ')))
sep = nome.split()
print('O primeiro nome é {} e tem {} letras'.format(sep[0], len(sep[0])))