'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

fatorial = int(input('Escolha um número: '))
multiplicação = fatorial * (fatorial-1)
fatorial = fatorial - 1
while fatorial != 1:
    fatorial = fatorial - 1
    multiplicação = multiplicação * fatorial
print(multiplicação)
