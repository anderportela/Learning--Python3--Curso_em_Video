#Definindo funções:
def fatorial(n=1, show=False):
    """
    --> Função que calcula o fatorial de um número digitado
    :param n: O número digitado
    :param show: (opcional) Mostrar ou não a conta do fatorial
    :return: O valor do fatorial do número digitado
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa principal:
print(fatorial(9, show=True))


