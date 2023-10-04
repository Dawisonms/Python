'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.'''
from time import sleep
def titulo(msg):
    print('\033[30;43m-' * (len(msg)+2))
    print(msg)
    print('-' * (len(msg)+2))
    print('\033[m')


def corpo():
    print('\033[32;40m')


def final(msg):
    print('\033[31;47m')
    print('-' * (len(msg)+2))
    print(msg)
    print('-' * (len(msg)+2))


while True:
    titulo('SISTEMA DE AJUDA PYTHON')
    funcao = input(str('Função ou Biblioteca > '))
    if funcao.upper() == 'FIM':
        final('Até Logo')
        break
    else:
        final(f'Acessando a função {funcao}')
        sleep(1)
        corpo()
        help(funcao)
