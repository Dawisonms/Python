'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = list()
for l in range(1, 6):
    valores.append(int(input(f'Valor {l}: ')))
    maior = max(valores)
    menor = min(valores)
print(f'A lista é {valores}')
print(f'O maior valor foi {maior} na posição', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {menor} na posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')




