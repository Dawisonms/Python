'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

fatorial = int(input('Qual fatorial: '))
multiplicação = 0

for f in range(fatorial - 1, 0, -1):
    multiplicação = fatorial * f
    fatorial = multiplicação
print(multiplicação)
