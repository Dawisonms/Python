#Programa que le o comprimento do cateto adjacente de um triangulo
#retangulo,calculee mostre o comprimento da  hipotenusa

import math
cat1 = float(input('Comprimento primeiro cateto: '))
cat2 = float(input('Comprimento segundo cateto: '))

hip = math.hypot(cat1,cat2)

print('A hipotenusa dos catetos {} e {} é igual a {:.2f}'. format(cat1, cat2,  hip))