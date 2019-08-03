print('-='*50)
print(f'\033[1;31m{"CADASTRO DE PESSOAS":^100}\033[m')
print('-='*50)
pessoas = []
pessoa = {}
si = mi = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Opção Inválida. Digite apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    si += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if r in 'NS':
            break
        print('Opção Inválida. Digite apenas S ou N!')
    if r == 'N':
        break
mi = si/len(pessoas)
print('*'*100)
print(f'Foram cadastradas {len(pessoas)} pessoas. ')
print(f'\nA média de idade das pessoas cadastradas é de {mi:.2f} anos')
print('\nAs mulheres cadastradas são: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
print('\n\nAs pessoas que têm idade acima da média são: ', end='')
for p in pessoas:
    if p['idade'] > mi:
        print(f'{p["nome"]} com {p["idade"]} anos')