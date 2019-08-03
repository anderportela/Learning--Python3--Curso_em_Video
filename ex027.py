nome = input('Digite seu nome completo: ').strip()
sep = nome.split()
print('o primeiro nome é:{}'.format(sep[0]))
print('O ultimo nome é: {}'.format(sep[len(sep)-1]))