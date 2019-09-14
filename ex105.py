
#                                 Definindo funções:

def notas(*n, sit=False):
    """
    --> Função que calcula a média de um aluno e exibe a situação do mesmo.
    Se a média for de 7 pra cima, Aprovado.
    Se a média for entre 5 e 7. Em exame
    Se a média for menor que 5. Reprovado
    :param n: valor das notas (não há limite de quantidade)
    :param sit: situação do aluno
    :return: dicionário com as notas e stuação do aluno
    """
    aluno = dict()
    mai = men = 0
    aluno['Notas'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    aluno['Média'] = sum(n) / len(n)
    if aluno['Média'] < 5:
        sit = 'Reprovado'
    elif 5 <= aluno['Média'] < 7:
        sit = 'Em exame'
    else:
        sit = 'Aprovado'
    aluno['Situação'] = sit
    return aluno



#                                 Programa principal:

print('-*-'*20)
print()
resp = notas(6, 8, 7, 5, 10, sit=True)
print(resp)
