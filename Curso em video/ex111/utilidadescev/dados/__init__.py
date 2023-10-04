def leiadinheiro(p):
    '''
    Usado para validar qualquer valor. Não aceita outra expressão. Ainda apresenta erro quando usado letras e números juntos.
    :param p: Informa o valor a ser analisado
    :return: Aceita somente números traduzindo o ponto(.) para vírgula(,)
    '''
    valido = False
    while not valido:
        resp = input(p).replace(',','.').strip()
        if resp.isalpha() or resp == '':
            print(f'"{resp}" incorreto, digite novamente')
        else:
            valido = True
            return float(resp)



def leiaint(num):
    '''
    Valida se um valor escrito é um número inteiro
    :param num: Qualquer número inteiro
    :return: Se é ou não o número e solicita uma nova inclusão.
    '''
    while True:
        try:
            resp = int(input(num))
        except (ValueError):
            print('\033[31mErro: Por favor, digite um número válido!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mErro: O usuário não digitou o numero!\033[m')
            return 0
        else:
            return int(resp)


def leiafloat(num):
    '''
    Valida se um número é tipo float
    :param num: Qualquer numero float
    :return: Se é um número float e se não for, solicita que informe corretamente o valor.
    '''
    while True:
        try:
            resp = float(input(num).replace(',', '.'))
        except Exception:
            print('\033[31mErro: Valor inválido. Digite novamente!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mErro: O usuário Não digitou o número!\033[m')
            return 0
        else:
            return resp