jogador = {}
partidas = []
print('-='*50)
print(f'\033[1;36m{"APROVEITAMENTO DE ATACANTES":^100}\033[m')
print('-='*50)
jogador['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
for p in range(0, part):
    partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {p+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
gp = jogador['total'] / part
print(f'\n{jogador["nome"]} marcou {jogador["total"]} gols no campeonato. Tendo média de {gp:.2f} gols por partida')
print('*'*100)
print(f'\n{jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'\n  => Na {i+1}ª partida, {jogador["nome"]} fez {v} gols')
print(f'\n   Totalizando {sum(partidas)} gols em sua participação')
