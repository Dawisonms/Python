'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep

print('<>'*20)
print(f'{"MEGA SENA":^40}')
print('<>'*20)
jogos = []
count = 6
qtd = int(input('Quantos jogos você deseja criar? '))
print('<>'*20)
print('Iniciando...')
sleep(1)
for v in range(0, qtd):
    for j in range(1, 7):
        jogos.append(randint(1, 60))
for pos, i in enumerate(jogos):
    print(f'{pos+1}º Jogo {jogos[:count]}')
    sleep(0.4)
    del jogos[:6]
print('<>'*20)
print(f'{qtd} Jogos gerados com sucesso!!')
print('<>'*20)
print(f'{"BOA SORTE!!!":^40}')
print('<>'*20)
