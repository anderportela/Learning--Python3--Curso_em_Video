from time import sleep
#                  Definindo funções:
def ajuda(com):
    efeito('Acessando banco de dados...', 3)
    sleep(1)
    print(c[2], end='')
    com = help(comando)
    print(c[0], end='')
    return com


def efeito(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('*' * tam)
    print(msg)
    print('*' * tam)
    print(c[0], end='')


#                  Programa principal:
c = ('\033[m', '\033[1;32m', '\033[1;31m', '\033[1;34m', '\033[1;33m')
efeito('VOCÊ ESTÁ EM DÚVIDA SOBRE ALGUM COMANDO?', 1)
print()
while True:
    comando = str(input('Digite o comando: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print()
efeito('ESPERAMOS TER AJUDADO!!!!', 4)
