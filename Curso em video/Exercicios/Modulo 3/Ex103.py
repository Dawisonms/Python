'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
 o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
  mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome=None, gols=0):
    '''

    :param nome: Nome do jogador ou nenhum valor
    :param gols: Número de gols ou sem valor
    :return:
    '''
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(gols) == 0:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols')



#Programa principal
n = str(input('Nome Jogador: ')).upper()
g = input('Número de gols: ')
ficha(n, g)