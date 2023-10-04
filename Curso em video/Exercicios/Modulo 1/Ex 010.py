#Programa que leia quanto uma pessoa tem  na carteira e mostra
# quantos dolares ela pode comprar. Considerar dolar USS 1,00=R$ 3,27)

carteira = float(input('Valor na carteira: '))
cambio = float(3.27)
dolar = carteira/cambio


print('Valor em R$ {},posso comprar {:.2f}'.format(carteira,dolar))