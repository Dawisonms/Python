#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

import math

r1 = float(input('Comprimento 1: '))
r2 = float(input('Comprimento 2: '))
r3 = float(input('Comprimento 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[33m Habilitado pra formar um triangulo')
else:
    print('\033[31m Não é possível fazer um triangulo')
