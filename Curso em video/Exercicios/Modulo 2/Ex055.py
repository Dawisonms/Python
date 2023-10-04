'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.'''

pesado = 0
leve = 0
print('Quais são os pesos: ')
for c in range(0, 5):
    peso = float(input('Peso: '))
    if peso > pesado:
        pesado = peso
    elif leve < peso:
        leve = peso

print('O maior peso lido foi de {}kg e o menor foi {}kg'.format(pesado, leve))

