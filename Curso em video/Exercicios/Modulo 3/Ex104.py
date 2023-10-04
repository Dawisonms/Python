'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

def leiaint(num):
    '''

    :param num: Valida se é um numero inteiro
    :return: Mensagem informando se o número é válido ou não. Caso seja inválido, pede pra digitar novamente.
    '''
    from time import sleep
    print('-'*20)
    resp = input(num)
    while True:
        if resp.isnumeric() is False:
            print('Tente outra vez, número inteiro inválido...')
            print('-'*20)
            sleep(1)
            resp = input(num)
        else:
            print(f'Você digitou o número {resp}')
            break


#Programa principal
n = leiaint('Digite um número: ')
print(type(n))
