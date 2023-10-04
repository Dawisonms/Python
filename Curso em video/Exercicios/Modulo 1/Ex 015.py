#Locação 60,00 o dia e KM  0,15

Dias = int(input('Quantos dias  ficou: '))
km = int(input('Quantos KM: '))
Locação: float = 60.00
Vkm: float = 0.15

print('Por {} dia (as) e com {} KM rodados o preço total é de {}'.format(Dias, km, (Dias*Locação) + (Vkm*km)))
