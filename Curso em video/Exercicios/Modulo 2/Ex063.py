'''Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

from fibonacci import fibo
elementos = int(input('Quantos elementos fibonacci você quer ver: '))
cont = 0
while elementos != cont:
    print(fibo(cont),end=', ')
    cont += 1
print('FIM')
