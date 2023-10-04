'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randrange
aleatorio = (randrange(1000), randrange(1000), randrange(1000), randrange(1000), randrange(1000))
cont = maior = menor = 0
print(f'A tupla aleatorio é {aleatorio}.')
for a in aleatorio:
    cont += 1
    if cont == 1:
        menor = a
    if a < menor:
        menor = a
    if a > maior:
        maior = a
print(f'O menor valor dessa tupla é {menor} e o maior é {maior}.')


