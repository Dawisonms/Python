# Programa que leia a largura e altura de uma parede em metros,calcule a sua area e a quantidade
# de tinta necessaria para pintá-la,sabendo que cada litro de tinta pinta uma área de 2m2.

altura = float(input('Altura parede: '))
largura = float(input('Largura da parede:'))
area = altura * largura
rendimento = 2
tinta = area / rendimento

print(
    ' Para uma parede de {} metros de altura e\n {} metros de largura, temos {} m2 de área. \n Com isso, precisaremos de {} litros de tintas'.format(
        altura, largura, area, tinta))

