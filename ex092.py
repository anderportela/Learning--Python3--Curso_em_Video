from datetime import date
pessoa = {}
print('-='*50)
print(f'\033[31m{"APOSENTADORIA?":^100}\033[m')
print('-='*50)
pessoa['nome'] = str(input('Digite seu nome: '))
nasc = int(input('Qual o ano de seu nascimento? '))
hj = date.today()
pessoa['idade'] = hj.year - nasc
pessoa['ctps'] = int(input('Digite o número de sua CTPS. Digite \033[31m 0 \033[m caso não possua CTPS: '))
if pessoa['ctps'] == 0:
    print(f'\n{pessoa["nome"]} está com {pessoa["idade"]} anos e não possui CTPS.')
else:
    pessoa['contratação'] = int(input('Digite o ano de sua contratação: '))
    aposentar = pessoa['contratação'] + 35
    pessoa['salário'] = float(input('Digite seu salário: '))
    print(f'\n{pessoa["nome"]} está com {pessoa["idade"]} anos ')
    print(f'\nPossui a CTPS de número: {pessoa["ctps"]}')
    print(f'\nFoi contratado em {pessoa["contratação"]} recebendo R$ {pessoa["salário"]:.2f}')
    print(f'\n{pessoa["nome"]} irá se aposentar com {aposentar - nasc} anos')