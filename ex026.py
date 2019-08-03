frase = input('Escreva uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes na frase digitada. '.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na posição {} da frase digitada.'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição {} da frase digitada.'.format(frase.rfind('A')+1))