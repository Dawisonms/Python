'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''

import random
import emoji
from time import sleep
while True:
    computador = random.randint(1, 3)
    print(emoji.emojize('Pedra:oncoming_fist:[1]'))
    sleep(1)
    print(emoji.emojize('Papel:hand_with_fingers_splayed:[2]'))
    sleep(1)
    print(emoji.emojize('Tesoura:victory_hand:[3]'))
    sleep(1)
    jogador = int(input(': '))
    pedra = 1
    papel = 2
    tesoura = 3

    if  computador == jogador:
        print('Empatou')
    elif computador == 1 and jogador == 2:
        print('Você ganhou')
    elif  computador == 2 and jogador == 1:
        print('Você perdeu')
    elif computador == 3 and jogador == 1:
        print('Voce ganhou')
    elif computador == 3 and jogador == 2:
        print('Você perdeu')
    elif computador == 1 and jogador == 3:
        print('Você perdeu')
    elif jogador > 3:
        print('Escolha outra opção')
    else:
        print('Você ganhou')

    if jogador == 1:
        print(emoji.emojize('Jogador =:oncoming_fist:'))
    elif jogador == 2:
        print(emoji.emojize('Jogador =:hand_with_fingers_splayed:'))
    elif jogador >3:
        print('Sem trapacear!!!')
    else:
        print(emoji.emojize('Jogador =:victory_hand:'))

    if computador == 1:
        print(emoji.emojize('Computador = :oncoming_fist:'))
    elif computador == 2:
        print(emoji.emojize('Computador =:hand_with_fingers_splayed:'))
    else:
        print(emoji.emojize('Computador =:victory_hand:'))
    print('-='*40)
    print('Vamos jogar outra vez...')
    sleep(2)

