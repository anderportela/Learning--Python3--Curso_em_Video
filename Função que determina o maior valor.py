from time import sleep
print('*'*50)

#Definindo funções:

def maior(num):
    mai = 0
    c = 0
    print('\nAnalisando os valores definidos...')
    sleep(1)
    if num == '':
        print('\n\033[31mNao foram definidos valores dessa vez...\033[m')
    sleep(1)
    for n in num:
        c += 1
        if n > mai:
            mai = n
    if num != '':
        print(f'\n{num} foram informados. Foram definidos \033[2;34m{c}\033[m valores')
        print(f'\nO maior número definido é \033[1;31m{mai}\033[m')
    print('*'*50)

#Programa principal:

num = 3, 4, 2
maior(num)
num = 9,1
maior(num)
num = ''
maior(num)
num = 4,0,6,1
maior(num)
