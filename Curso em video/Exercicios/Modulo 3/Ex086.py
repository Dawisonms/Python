'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''
matriz = []
for m in range(0, 3):
    for n in range(0, 3):
        matriz.append([int(input(f'Digite o valor para {m, n}: '))])
print(matriz[0:3])
print(matriz[3:6])
print(matriz[6:9])
