'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
from time  import sleep
print('^'*30)
print('VAMOS JOGAR PAR OU IMPAR???')
print('^'*30)
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Qual seu número: '))
    escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    while True:
        if escolha not in 'IiPp':
            escolha = str(input('Opção incorreta!! Escolha [P/I]: '))
        else:
            break
    resultado = computador + jogador
    print(f'Computador  {computador}')
    print(f'Resultado {resultado}')
    if resultado % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
        if escolha != resultado != 'P':
            break
    print('Você venceu!')
    sleep(2)
    print('-' * 30)
    print('Vamos jogar novamente?')
    cont += 1
print(f'Você perdeu!\033[33m\nNo total você ganhou {cont} partidas seguidas!!')

