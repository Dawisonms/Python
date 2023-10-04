from bibliotecas.arquivo import *
from time import sleep
from Forca.bibliotecas.config import *
from unidecode import unidecode


palavras = 'dados.txt'
if not arquivoexiste(palavras):
    criararquivo(palavras)

titulo('JOGO DA FORCA')

alertas(f'{"Vamos jogar???":^40}')
sleep(1)
alertas('Quem vai jogar? ')
sleep(1)
jogador = leiastr('Nome: ')
sleep(1)
alertas(f'Olá {jogador}... Escolha a opção abaixo: ')
while True:
    menu(['Ver palavras existentes', 'Incluir novas palavras', 'Jogar - Aleatório', 'Sair'])
    opção = leiaint('\033[32mSua opção:\033[m ')
    if opção == 1:
        lerarquivo(palavras)
        sleep(2)
    elif opção == 2:
        n_palavra = leiastr('Palavra: ').upper()
        Grupo = leiastr('Grupo: ')
        incluir(palavras, n_palavra, Grupo)
        sleep(2)
    elif opção == 3:
# Desenvolvimento do jogo
        count = 0
        with open(palavras, 'r') as a: #Conta quantas linhas tem a base de dados para limitar o range de escolha da palavra.
            for seq in a:
                count += 1
        print(f'Escolha um número entre 1 e {count}')
        print('-' * 20)
        # Escolha da palavra pelo usuário
        palavra = list()
        escolha = int(input('Escolha: '))
        with open(palavras, 'r') as a:
            for seq, pal in enumerate(a):
                p = pal.split(';')
                if seq + 1 == escolha:
                    palavra.append(p[0])
                    dica = p[1]
                    break
        resposta = list()
# Contar a quantidade de letras da palavra escolhida
        q_letras = 0
        for pos, letra in enumerate(palavra[0]):
            q_letras += 1
            resposta.append('_')
        print(
            f'{"_ " * q_letras} => Você tem {q_letras} tentativas pra acertar a palavra com a dica : \033[1;4;35m{dica}\033[m',
            end='')
        letras = list()
        tentativas = 0
#Verifica se a letra escolhida consta na palavra selecionada aleateriamente.
        while True:
            tentativas += 1
            if '_' in resposta:
                sleep(2)
                if tentativas < q_letras:
                    print(f'\033[33m{tentativas}ª tentativa\033[m')
                elif tentativas == q_letras:
                    print('\033[31mUltima tentativa!!!\033[m')
            else:
                print(f'\033[1;4;35mParabéns {jogador}, você VENCEU!!\033[m')
                titulo('O que deseja fazer?')
                sleep(2)
                print('-'*40)
                break
            if tentativas > q_letras:
                print('\033[1;4;31mVocê perdeu!!\033[m')
                titulo('O que deseja fazer?')
                break
            resp = leiastr('Letra: ').upper()  # Letras já informadas
            letras.append(resp)  # Letras já informadas
            for pos, lt in enumerate(unidecode(palavra[0])):  # Insere a letra no lugar correto quando acertado.
                if lt == resp:
                    resposta.insert(pos, resp)
                    resposta.pop(pos + 1)
            for lr in resposta:  # print das palavras corretas na sequencia
                print(f'\033[1;4;32m{lr}\033[m', end=' ')
            print()
            print(f'\033[34mLetras já informadas {letras}\033[m')
            print('-*-' * 10)
#Saida do Jogo
    elif opção == 4:
        alertas('Saindo do Jogo...Até logo!')
        break
    else:
        print('Opção incorreta. Digite novamente!')
        sleep(1)

#1 - Pendende te acerto número de tentativas. O sistema não estava considerando os acertos obtidos
#2 - Pendente de acerto no item 2 de inclusão de novas palavras. Validar se já não existe a nova palavra.
