#Crie um programa converte um numero real (com ponto) e converte para inteiro,sem ponto

import math

num = float(input('Dig um numero com ponto: '))

num2 = math.floor(num)

print(' o numemero inteiro é {}'.format(num2))