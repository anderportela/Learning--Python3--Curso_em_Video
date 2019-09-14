#Definindo funções:
def ficha(jog='Desconhecido', gol=0 ):
    print(f'\n\033[1;31m{jog}\033[m marcou \033[1;32m{gol}\033[m gols durante o campeonato!')


#Programa principal
print('*'*50)
nome = str(input('Digite o nome do(a) jogador(a): '))
marcou = str(input('Digite a quantidade de gols marcados: '))
if marcou.isnumeric():
    marcou = int(marcou)
else:
    marcou = 0
if nome.strip() == '':
    ficha(gol = marcou)
else:
    ficha(nome, marcou)
