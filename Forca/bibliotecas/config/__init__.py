def titulo(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)

def alertas(msg):
    print(f'\033[33m{msg}\033[m')

def leiastr(txt):
    '''
    Valida se um valor escrito é uma string
    :param num: Qualquer string
    :return: Se é ou não a str e solicita uma nova inclusão.
    '''
    while True:
        try:
            resp = str(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite somente uma palavra/texto!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[33mErro: O usuário não digitou a palavra/texto!\033[m')
            return 0
        else:
            return str(resp)


def leiaint(num):
    '''
    Valida se um valor escrito é um número inteiro
    :param num: Qualquer número inteiro
    :return: Se é ou não o número e solicita uma nova inclusão.
    '''
    while True:
        try:
            resp = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um número válido!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[33mErro: O usuário não digitou o numero!\033[m')
            return 0
        else:
            return int(resp)


def menu(lista):
    '''print('-' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)'''
    for pos, n in enumerate(lista):
        print(f'\033[33m{pos + 1} - \033[34m{n}\033[m')
    print('-' * 30)


def umaletra(letra):
    '''

    :param letra: Valida se foi difitado somente uma letra
    :return: Letra digitada ou solicitando a correção
    '''
    while True:
        caract = input(letra)
        if len(caract) == 1:
            return caract
            break
        else:
            print('\033[31mErro: Por favor, digite somente uma letra!!\033[m')

