lista = []
for n in  range(0, 5): #Repetir 'n' por 5 vezes
    v = int(input('Digite um valor inteiro: '))
    if n == 0 or v > lista[-1]: #Caso seja o primeiro valor digitado ou o valor for maior que o ultimo valor da lista
        lista.append(v) #acrescenta o valor digitado ao final da lista
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): #Enquanto 'pos' for menor que o valor de comprimento da lista
            if v <= lista[pos]: #Caso valor digitado for menor ou igual a posição 'pos' da lista
                lista.insert(pos, v) #Inserir o valor digitado na posição 'pos'
                print(f'Adicionado na {pos + 1}ª posição...')
                break
            pos += 1 #Acrescentar 1 em 'pos'
print('*'*50)
print(lista)