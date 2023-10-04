#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite.

import emoji
velocidade = float(input('Qual sua velocidade? : '))

if velocidade > 80:
    print('Você foi multado!!')
    print('A multa será de R$ {:.2f}'. format((velocidade - 80) * 7.00))

else:
    print(emoji.emojize('Continue assim!!! {}'.format(':red_heart:' * 3)))