'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.'''

termo = int(input('Qual termo da PA: '))
razão = int(input(('Qual a razão dessa PA: ')))
termo = termo - razão
PA = termo
print('Os 10 primeiros termos dessa PA é: ')
for c in range(0, 10):
    PA = PA + razão
    print(PA, end= '→ ') # seta foi colocada com alt 26
