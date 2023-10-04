'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
 aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
  sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep

jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
jog = []
primeiro = 0
for j, v in jogadores.items():
    print(f'O {j} tirou o número {v}')
    sleep(0.8)
    jog.append([v, j])
jog.sort(reverse=True)
print('-='*30)
for seq, o in enumerate(jog):
    print(f'O {o[1]} foi o {seq+1}º colocado com o número {o[0]}')
    sleep(0.8)
