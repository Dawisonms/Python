'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
 Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contador(i, f, p):
    from time import sleep
    if i > f and p > 0:
        p = p * -1
    if f > i and p < 0:
        p = p * -1
        print(f'Considerado o valor {p}')
    if p == 0:
        p = 1
        print('Considerado o valor 1')
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.5)
    print()
    print('=-'*20)


print('Contagem de 1 a 10')
contador(1, 11, 1)
print('Contagem de 10 a 0 com passo 2')
contador(10, 0, -2)
print('Agora é sua vez...')
contador(int(input('\033[33mInicio: ')), int(input('Fim: ')), int(input('Passo: ')))