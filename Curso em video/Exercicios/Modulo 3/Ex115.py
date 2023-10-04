'''Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
'''
import
from time import sleep
while True:
    menu()
    opção = dados.leiaint('Sua opção: ')
    if 1 <= opção <= 2:
        titulos(f'OPÇÃO {opção}')
        break
    elif opção == 3:
        titulos('Saindo do sistema...Até logo!')
        break
    else:
        print('Opção incorreta. Digite novamente!')
        sleep(1)





