sal = float(input('Qual é o seu salário? '))
casa = float(input('Qual o valor da casa que você quer comprar? '))
tempo = int(input('Em quantos anos você quer pagar pela casa? '))
parc = casa/(tempo * 12)
if parc > (0.3 * sal):
    print('Seu empréstimo foi reprovado. A parcela excede o limite de 30% de seu salário!')
else:
    print('Você pagará R${:.2f} por mês! '.format(parc))