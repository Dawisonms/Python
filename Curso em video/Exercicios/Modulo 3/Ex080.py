'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
from typing import List, Any

valores = []
for lista in range(1, 6):
    valor = int(input(f'Valor {lista}: '))
    if lista == 1:
        valores.append(valor)
        print('incluido na ultima posição')
    else:
        if valor < min(valores):
            valores.insert(0, valor)
            print('Incluido na posição 0')
        elif valor > max(valores):
            valores.append(valor)
            print('Incluido na ultima posição')
        else:
            min(valores) < valor < max(valores)
            if valor < valores[1]:
                valores.insert(1, valor)
                print('Incluido na posição 1')
            elif valores[1] < valor < valores[2]:
                valores.insert(2, valor)
                print('Incluido na posição 2')
            else:
                valores.insert(3, valor)
                print('Incluido na posição 3')
    print(valores)

