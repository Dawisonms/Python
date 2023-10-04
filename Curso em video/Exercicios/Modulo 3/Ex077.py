'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

veiculos = ('Carro','Moto','Caminhao', 'Tratores', 'SUV', 'Pick up')

for v in veiculos:
    print(f'\nA palavra {v.upper()}, temos as vogais: ',end='')
    for letra in v:
            if letra.lower() in 'aeiou':
                print(letra.upper(),end=' ')




