'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
 terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(Largura, Comprimento):
    a = Largura * Comprimento
    print(f'\033[34m{a:.2f} m2')

Largura = float(input('\033[33mLargura: '))
Comprimento = float(input('Comprimento: '))
area(Largura, Comprimento)
