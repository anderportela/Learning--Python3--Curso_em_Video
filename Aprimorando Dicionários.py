jogador = {}
partidas = []
jogadores = []
print('-='*50)
print(f'\033[1;36m{"APROVEITAMENTO DE ATACANTES":^100}\033[m')
print('-='*50)
while True:
    jogador.clear()
    jogador['nome'] = str(input('\nNome do jogador: '))
    part = int(input(f'\nQuantas partidas {jogador["nome"]} disputou? '))
    partidas.clear()
    for p in range(0, part):
        partidas.append(int(input(f'\nQuantos gols {jogador["nome"]} marcou na partida {p+1} ?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    gp = jogador['total'] / part
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('\nQuer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida. Digite S ou N.')
    if resp == 'S':
        continue
    else:
        break
print('*'*100)
print('Cód.', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k+1:^3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*'*100)
while True:
    busca = int(input('\nDe qual jogador você quer os dados? (Digite 999 para cancelar) '))
    if busca == 999:
        break
    if busca >= (len(jogadores)+ 1):
        print(f'\nNão existe jogador com código {busca}')
    else:
        print(f'\n\033[31mDados do jogador {jogadores[busca-1]["nome"]}:\033[m ')
        for i, g in enumerate(jogadores[busca-1]['gols']):
            print(f'\nNa {i+1}ª partida, marcou {g} gols')
    print('-='*45)

