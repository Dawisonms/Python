'''Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro
 de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
print('{}CONTAGEM REGRESSIVA PARA OS FOGOOS!!!{}'.format('='*20, '='*20))
from time import sleep
from emoji import emojize
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
for f in range(0,5):
    print(emojize(':fireworks: :sparkler:'))
    sleep(1)
