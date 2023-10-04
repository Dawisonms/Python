'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import  date

ano = date.today().year
maior = 21
maiores = 0
menores = 0
print('Quais anos de nacimento: ')
for c in range(1,8):
    nascimento = int(input('{}º Ano: '.format(c)))
    if ano - nascimento >= maior:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('{} pessoas ainda não atingiram a maior idade e {} já são maiores'.format(menores, maiores))
