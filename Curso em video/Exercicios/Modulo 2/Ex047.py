'''Exercício Python 047: Crie um programa que mostre na tela
 todos os números pares que estão no intervalo entre 1 e 50.'''

for c in range(1,51): # ou pode colocar range(2,51,2).. reduz a memoria usada no computador.
    if c % 2 == 0:
        print(c, end= ' ') # end= ' ' => imprime na mesma linha o que o python imprimiria uma linha abaixo da outra
