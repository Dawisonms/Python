'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
  mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
numeros = 0
flag = 999
soma = 0
count = 0
while numeros != flag:
    numeros = int(input('Digite um numero: '))
    if numeros != flag:
        soma = soma + numeros
        count = count + 1
print('A soma dos {} numeros, totalizam {}'.format(count, soma))
