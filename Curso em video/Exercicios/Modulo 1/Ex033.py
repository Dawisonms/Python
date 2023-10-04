# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

cores = {'limpar': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'ciano': '\033[36m'}

num1 = int(input('{} Escolha um numero: {}'.format(cores['azul'],cores['limpar'])))
num2 = int(input('{} Escolha outro numero: {}'.format(cores['ciano'],cores['limpar'])))
num3 = int(input('{} Ultimo número: {}'.format(cores['amarelo'],cores['limpar'])))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O menor numero é {}'.format(menor))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior numerio é {}'.format(maior))

'''' mesmo resultado com caminho diferente
lista = [num1, num2, num3]

maior = max(lista)
menor = min(lista)

print('O maior numero é {} e o menor é {}'.format(maior,menor))'''
