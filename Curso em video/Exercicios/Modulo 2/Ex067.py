'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo. '''
from time import sleep
print('-'*20)
print('TABUADA')
print('-'*20)
while True:
    num = int(input('Qual tabuada quer saber: '))
    if num < 0:
        break
    for t in range(0, 11):
        print(f'{num} x {t} = {num * t}')
    print('='*20)
    sleep(2)
print('Acabou')