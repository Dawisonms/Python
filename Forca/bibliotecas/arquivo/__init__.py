from bibliotecas.config import *

def arquivoexiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


#-----------------------------------------------------------------------
def criararquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('\033[31mERRO: Não foi possível criar o arquivo\033[m')
        return False
    else:
        print(f'\033[34mArquivo {arquivo} criado com sucesso!\033[m')
        return True

#--------------------------------------------------------------------------
def lerarquivo(arquivo):
    try:
        a = open(arquivo, 'r')
    except FileNotFoundError:
        print('\033[31mERRO: Arquivo não encontrado!\033[m')
        return False
    except Exception as e:
        print(f'033[31mERRO: Ocorreu o erro {e} ao abrir o arquivo!')
        return False
    else:
        titulo('OPÇÃO 1')
        for lista in a:
            dados = lista.split(';')
            dados[2] = dados[2].replace('\n','')
            print(f'{dados[0]} - {dados[1]:.<30}{dados[2]}')
    finally:
        a.close()


#----------------------------------------------------------------------
def incluir(arquivo,num=False, msg='<Desconhecido>', tipo=''):
    try:
        a = open(arquivo, 'at')
    except:
        print('ERRO: Arquivo não encontrado')
    else:
        try:
            a.write(f'{num};{msg};{tipo}\n')
        except TypeError as erro:
            print(f'ERRO ao tentar incluir o nome {erro}')
        else:
            titulo(f'Seq {num} e palavra {msg} com tipo {tipo}, incluidos com sucesso')
    finally:
        a.close()

