n = c = s = 0
while n != 999:
    n = int(input('\nDigite qualquer número. Digite 999 para encerrar o programa: '))
    s += n
    c += 1
print('\nVocê digitou {} números e a soma entre eles é: {}'.format(c-1, s-999))
print('\nFIM')