'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.
'''

def sorteia(lista):
    from random import randint
    for n in range(0, 5):
        num = randint(1, 100)
        lista.append(num)

números = list()
sorteia(números)
print(f'Os números sorteados foram => {números}')

def somaPar(lista):
    par = 0
    for n in lista:
        if n % 2 == 0:
            par += n
    print(f'A soma de todos os números pares é => {par}')

somaPar(números)