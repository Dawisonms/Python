'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

par = 0
for c in range (1,7):
    numeros = float(input('Número {}: '.format(c)))
    if numeros % 2 == 0:
        par = par + numeros
print('A soma de todos os numeros pares é {}:'.format(par))
