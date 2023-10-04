'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla = (int(input('Valor 1: ')), int(input('Valor 2: ')),int(input('Valor 3: ')), int(input('Valor 4: ')))
print(f'Temos a contagem de {tupla.count(9)} numeros 9.')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na posição {tupla.index(3)}.')
else:
    print('O numero 3 não foi encontrado')
print('Os numeros pares dessa lista são ', end='')
for p in tupla:
    if p % 2 == 0:
        print(p, end=', ')

