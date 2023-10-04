'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

compra = ('Lápis', 2.00, 'Apontador', 0.50, 'Caneta', 3.00,'Estojo',5.00, 'Mochila', 90.00,'Caderno',25.00, 'Lapiseira', 12.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for cont, item in enumerate(compra):
    if cont % 2 == 0:
        print(f'{compra[cont]:.<30}', end='')
    else:
        print(f'R$ {compra[cont]:>5.2f}')
print('-'*40)
