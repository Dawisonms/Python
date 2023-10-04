'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Numero para validação (primo): '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[033m',  end='')
    else:
        print('\033[35m', end='')
    print(c, end=', ')

if cont == 2:
    print('\033[m \nO número digitado {},é um número PRIMO!!'.format(num))
else:
    print('\033[m \nO número {}, NÃO é um numero primo!!'.format(num))
