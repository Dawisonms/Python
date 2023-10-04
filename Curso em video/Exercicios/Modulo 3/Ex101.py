'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import datetime

def votar(num):
    '''

    :param num: Informar o ano de nascimento de uma pessoa para calcular a obrigatoriedade do voto
    :return: Menor que 16 não pode votar (NEGADO). Idades entre 16, 17 e maiores de 65 anos são OPCIONAIS e entre
    18 e 65 anos são OBRIGATÓRIO.
    '''
    idade = datetime.today().year - num
    if idade < 16:
        return f'Sua idade é {idade} anos e seu voto FOI NEGADO'
    elif 18 <= idade <= 65:
        return f'Sua idade é {idade} anos e o seu voto É OBRIGATÓRIO'
    else:
        return f'Sua idade é {idade} anos e o seu voto É OPCIONAL'


#Programa principal
print('-'*40)
voto = votar(int(input('Em que ano você nasceu?: ')))
print(voto)
print('-'*40)

