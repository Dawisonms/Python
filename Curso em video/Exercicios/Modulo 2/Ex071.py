'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
 o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
from math import trunc
while True:
    valor = int(input('Qual valor deseja sacar? R$ '))
    print('-'*40)
    print('Seu saque contemplam: ')
    ced50 = (valor % 50)
    ced20 = ced50 % 20
    ced10 = ced20 % 10
    ced1 = ced10 % 1
    q50 = trunc(valor / 50)
    q20 = trunc(ced50 / 20)
    q10 = trunc(ced20 / 10)
    q1 = trunc(ced10 / 1)
    print(f'{q50} Cédulas de R$ 50,00 \n{q20} Cédulas de R$ 20,00 \n{q10} Cédulas de R$ 10,00 \n{q1} Cédulas de R$ 1,00')
    print('-'*40)
    perg = str(input('Deseja sacar mais algum valor? [S/N]: ')).strip().upper()[0]
    while True:
        if perg not in 'SsNn':
            perg = str(input('Deseja encerrar? [S/N] ')).strip().upper()[0]
        else:
            break
    if perg in 'Nn':
        break
print('Obrigado, volte sempre!')
