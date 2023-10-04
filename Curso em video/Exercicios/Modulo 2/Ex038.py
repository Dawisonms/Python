''' Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero para comparação: '))

if n1 > n2:
    print('{} É maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} É maior que {}'.format(n2, n1))
else:
    print('Não existe maior valor, ambos os numeros {} e {} são iguais'.format(n1, n2))