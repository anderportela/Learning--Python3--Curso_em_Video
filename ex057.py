s = input('Digite seu sexo [M/F]: ').upper()[0].strip()
while s not in 'MF':
    s = input('Dados inválidos!\nInforme seu sexo corretamente: ').strip().upper()[0]
print('\nSexo {} registrado com êxito!'.format(s))