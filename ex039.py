ano = int(input('Digite o ano de seu nascimento:\n '))
idade = 2019 - ano
if idade < 18:
    print('Você ainda irá se alistar...')
    print('Ainda faltam {} anos para você se alistar'.format(18 - idade))
elif idade == 18:
    print('Você já está na idade de se alistar!')
    print('Dirija-se a uma junta militar!')
else:
    print('Você já passou da idade de se alistar!')
    print('Você deveria ter se alistado há {} anos atrás!'.format(idade - 18))