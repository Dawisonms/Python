'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('='*20,'LOJA DO PORTUGA','='*20 )

produto = float(input('Qual o valor da compra: '))
metodo_pgto = int(input('''Escolha uma das opções abaixo:
[1] Dinheiro ou cheque
[2] Cartão 
[3] Pagamento em 2 X
[4] Pagamento em 3 vezes ou mais 
=> :'''))

din_cheq_1 = produto - (produto * 10 / 100)
cartao_2 = produto - (produto * 5 / 100)
DuasX_3 = produto
tresX_4 = produto * 1.20

if metodo_pgto == 1:
    print('Com a forma de pagamento escolhida, o valor final do produto é de R$ {:.2f} (Desconto de 10%)'.format(din_cheq_1))
elif metodo_pgto == 2:
    print('Com a forma de pagamento escolhida, o valor final do produto é de R$ {:.2f} (Desconto de 5%)'.format(cartao_2))
elif metodo_pgto == 3:
    print('Com a forma depagamento escolhida, o valor final do produto é o mesmo R$ {:.2f}'.format(DuasX_3))
elif metodo_pgto == 4:
    par = int(input('Quantas parcelas: '))
    if par >= 3:
        print('Com a forma de pagamento escolhida, o valor final do produto é de R$ {:.2f} (Juros de 20%)'.format(tresX_4))
    else:
        print('Volte e escolha outra opção')

else:
    print('Número inválido. Volte e escolhe uma opção de 1 a 4. Obrigado!!')





