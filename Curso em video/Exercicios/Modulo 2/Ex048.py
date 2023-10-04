'''Exercício Python 048: Faça um programa que calcule a soma entre todos
 os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        s = s + c

print('soma = {} de {} numeros'.format(s, contador))

