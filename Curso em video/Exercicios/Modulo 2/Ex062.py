'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''
from time import sleep
primeiro = int(input('Qual termo: '))
razão = int(input('Qual a razão: '))
termo = primeiro
cont = 1
quant = 10
resposta = ''
while resposta != 0:
    while cont <= quant:
        print(termo, end=' → ')
        cont += 1
        termo = termo + razão
    print('\n')
    print('-='*20)
    sleep(2)
    resposta = int(input('\nDeseja acrescentar mais termos: '))
    if resposta >= 1:
        quant = quant + resposta
        print('Os valores adicionais da sua PA são: ')
print('FIM')
