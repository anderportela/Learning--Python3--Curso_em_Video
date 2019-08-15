from time import sleep
historico = dict()
print('-='*65)
print(f'{"SERÁ QUE VOCÊ FOI APROVADO?":^120}')
print('-='*65)
historico['nome'] = str(input('Digite o nome: '))
historico['media'] = float(input(f'Média de {historico["nome"]}: '))
if historico['media'] >= 7:
    historico['situacao'] = 'aprovado(a)!'
elif 5 <= historico['media'] < 7:
    historico['situacao'] = 'em recuperação!'
else:
    historico['situacao'] = 'reprovado(a)!'
print('*'*70)
print('ANALISANDO A SITUAÇÃO...')
sleep(1.5)
print()
print(f'{historico["nome"]} está {historico["situacao"]}')
