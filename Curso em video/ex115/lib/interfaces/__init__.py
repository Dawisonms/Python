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


#----------------------------------------------------------
def titulos(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-'* 30)


#----------------------------------------------------------
def menu(lista):
    print('-'*30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-'*30)
    for pos, n in enumerate(lista):
        print(f'\033[33m{pos + 1} - \033[34m{n}\033[m')
    print('-'*30)

