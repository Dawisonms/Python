#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Nome completo: ')

print('Existe Silva nesse nome {}?: {}'.format(nome, nome.find('Silva') >=0))


