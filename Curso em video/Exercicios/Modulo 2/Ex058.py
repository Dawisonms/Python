'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
numero = randint(0,10)
jogador = int(input('informe um número de 0 a 10: '))
cont = 1
while jogador != numero:
    if jogador > numero:
        print('Menos...Tente outra vez!!')
        jogador = int(input('Qual seu palppite: '))
    elif jogador < numero:
        print('Mais...Tente outra vez!')
        jogador = int(input(('Qual seu palpite: ')))
    cont += 1
print('Você errou {} vezes antes de vencer. Parabéns!!'.format(cont - 1))

