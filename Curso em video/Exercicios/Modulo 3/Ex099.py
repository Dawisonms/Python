'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(lst):
    print(max(lst))
    print('-'*30)

l1 = [1, 5, 10, 9]
l2 = [5, 10, 66, 89, 10, 0]
l3 = [8]
l4 = [0]
print(f'A lista {l1}, contem {len(l1)} itens e o maior é:')
maior(l1)
print(f'A lista {l2}, contém {len(l2)} items e o maior é: ')
maior(l2)
print(f'A lista {l3}, contém {len(l3)} items e o maior valor é: ')
maior(l3)
print(f'A lista {l4}, contém {len(l4)} items e o maior valor é: ')
maior(l4)
