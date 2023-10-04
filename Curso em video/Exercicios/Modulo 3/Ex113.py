'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
 de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
from ex111.utilidadescev import dados
inteiro = dados.leiaint('Número Inteiro: ')
real = dados.leiafloat('Numero Real: ')
print(f'Você digitou os valores {inteiro} e {real}')
