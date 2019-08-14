from time import sleep
geral = list()
print('                             \033[32mMÉDIAS DE ALUNOS\033[m        ')
print('-='*35)
while True:
    a = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    md = (n1 + n2) / 2
    geral.append(([a, [n1, n2], md]))
    r = str(input('Quer continuar? [S/N]')).upper()
    if r == 'N':
        break
print(f'\n\033[34m{"Num.":<6}{"NOME":<12}{"MÉDIA":<8}\033[m')
for i, a in enumerate(geral):
    print(f'{i+1:<6}{a[0]:<12}{a[2]:<8.1f}')
while True:
    print('-='*35)
    na = int(input('\nVocê deseja ver as notas de qual aluno? (Pesquise pelo número. Digite 999 para cancelar.'))
    if na == 999:
        break
    if na <= len(geral) - 1:
        print(f'\nAs notas de {geral[na-1][0]} são {geral[na-1][1]} ')
sleep(1.5)
print('\nFINALIZANDO PROGRAMA..........')
