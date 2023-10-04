from Aprendix.Diversos.lib.interfaces import*
from Aprendix.Diversos.lib.arquivo import*
from time import sleep
arq = 'dados.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair'])
    opção = leiaint('\033[32mSua opção:\033[m ')
    if opção == 1:
        lerarquivo(arq)
        sleep(2)
    elif opção == 2:
        nome = input('Novo nome: ').upper()
        idade = leiaint('Idade: ')
        incluir(arq, nome, idade)
        sleep(2)
    elif opção == 3:
        titulos('Saindo do sistema...Até logo!')
        break
    else:
        print('Opção incorreta. Digite novamente!')
        sleep(1)

