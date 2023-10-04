#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
nc = random.randrange(0, 5)

num = int(input('Dig um numero entre 0 a 5: '))
print('\033[33mPROCESSANDO....')
sleep(4)
if nc == num:
    print('\033[34mParabén, você acertou')
else:
    print('\033[31mTente outra vez!')