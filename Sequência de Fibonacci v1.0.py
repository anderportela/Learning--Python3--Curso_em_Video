n = int(input('\nDigite a quantidade de termos da Sequência de Fibonacci (mín. 3 termos): '))
t1 = 0
t2 = 1
c = 3
while n < 3:
    n = int(input('\nOpção Inválida! A quantidade mínima de termos são três. Digite novamente: '))
print('\nA sua sequência de Fibonacci é:\n')
print('{} {} '.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print('{} '.format(t3), end ='')
    t1 = t2
    t2 = t3
    c += 1
print('\n\nFIM')
