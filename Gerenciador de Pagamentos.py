preco = float(input('Digite o preço do produto: \n'))
opc1 = input('Responda com S ou N: \nPagamento em dinheiro?\n')
if opc1 == 'S':
    print('O valor pago será R${:.2f}'.format(preco*0.9))
else:
    opc2 = input('Pagamento a vista?\n')
    if opc2 == 'S':
        print('O valor pago será R${:.2f} '.format(preco*0.95))
    else:
        opc3 = int(input('Em quantas parcelas?\n'))
        if 2 >= opc3 > 0:
            print('Cada parcela será de R${:.2f} e o total será R${:.2f}'.format(preco/opc3, preco))
        elif opc3 >=3:
            print('Cada parcela será R${:.2f} e o valor total será R${:.2f}'.format((preco*1.2)/opc3, preco*1.2))
        else:
            print('Opção Inválida')
