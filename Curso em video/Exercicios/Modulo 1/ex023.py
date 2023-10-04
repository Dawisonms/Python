#Exercício Python 023: Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.


cores = {'limpar': '\033[m',
         'branco': '\033[30m',
         'verde': '\033[32m',
         'magenta': '\033[35m',
         'negativo': '\033[7m'}
num = int(input('{}Dig um ano:{} '.format(cores['negativo'], cores['limpar'])))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('{} Unidade = {}'.format(cores['verde'], u))
print('{} Dezena = {}'.format(cores['magenta'], d))
print('{} Centena = {}'. format(cores['verde'], c))
print('{} Milhar = {}{}'.format(cores['magenta'], m ,cores['limpar']))



""" Modo mais avançado de fazer...
    if len(num) == 4:
        print('{} Milhar'.format(num[0]))
        print('{} Centena'.format(num[1]))
        print('{} Dezena'.format(num[2]))
        print('{} Unidade'.format(num[3]))
    
    if len(num) == 3:
        print('{} Centena'.format(num[0]))
        print('{} Dezena'.format(num[1]))
        print('{} Unidade'.format(num[2]))
    
    if len(num) == 2:
        print('{} Dezena'. format(num[0]))
        print('{} Unidade'.format(num[1]))
    
    if len(num) == 1:
        print('{} Unidade'.format(num[0]))"""
