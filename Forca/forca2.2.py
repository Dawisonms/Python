from bibliotecas.arquivo import *
from time import sleep
from bibliotecas.config import *
from unidecode import unidecode
palavras = 'dados.txt'
if not arquivoexiste(palavras):
    criararquivo(palavras)
while True:
    titulo('JOGO DA FORCA')
    menu(['Ver palavras existentes', 'Incluir novas palavras', 'Jogar - Aleatório', 'Sair'])
    opção = leiaint('\033[32mSua opção:\033[m ')
    if opção == 1:
        lerarquivo(palavras)
        sleep(1)
    elif opção == 2: # Inclusão de nova palavra com validação se existe no banco
        while True:
            count = 0
            with open(palavras,'r') as a:  # Conta quantas linhas tem a base de dados para limitar o range de escolha da palavra.
                for seq in a:
                    count += 1
            n_palavra = leiastr('Palavra: ').upper().strip()
            with open(palavras, 'r') as a:
                for seq in a:
                    n_p = seq.split(';')
                    n_p = n_p[1]
                    if unidecode(n_p) == unidecode(n_palavra):
                        n_p = True
                        break
                if n_p is True:
                    print('Palavra já existe')
                else:
                    Grupo = leiastr('Grupo: ')
                    incluir(palavras, count+1, n_palavra, Grupo)
                    sleep(1)
                    break
    # Desenvolvimento do jogo
    elif opção == 3:
        print('''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ''')
        titulo('INICIO')
        count = 0
        with open(palavras,'r') as a:  # Conta quantas linhas tem a base de dados para limitar o range de escolha da palavra.
            for seq in a:
                count += 1
        while True:
            escolha = int(input(f'Escolha um número entre 1 e {count}: '))
            if 0 < escolha <= count:
                break
        print('-' * 20)
        # Escolha da palavra pelo usuário
        palavra = list()
        with open(palavras, 'r') as a:
            for seq, pal in enumerate(a):
                p = pal.split(';')
                if seq + 1 == escolha:
                    palavra.append(p[1])
                    dica = p[2]
                    break
        resposta = list()
# Contar a quantidade de letras da palavra escolhida
        q_letras = 0
        for pos, letra in enumerate(palavra[0]):
            q_letras += 1
            resposta.append('_')
        print(f'{"_ " * q_letras} => Você tem {q_letras} tentativas pra acertar a palavra com a dica : \033[1;4;35m{dica}\033[m', end='')
        letras = list()
        tentativas = 0
#Verifica se a letra escolhida consta na palavra selecionada aleateriamente e valida o número de erros e acertos, além das letras já informadas
        while True:
            tentativas += 1
            if '_' in resposta:
                sleep(1)
                if tentativas < q_letras:
                    print(f'\033[33m{tentativas}ª tentativa de {q_letras}\033[m')
                elif tentativas == q_letras:
                    print('\033[31mUltima tentativa!!!\033[m')
            else:
                print(f'\033[1;4;35mParabéns, você VENCEU!!\033[m')
                sleep(1)
                break
            if tentativas > q_letras:
                print('\033[1;4;31mVocê perdeu!!\033[m')
                sleep(1)
                break
            resp = umaletra('Letra: ').upper().strip()  # Letras escolhida
            letras.append(resp)  # Append na lista de Letras já informadas
# Inserir a letra no lugar correto quando acertado sem acentos.
            verificação = False
            for pos, lt in enumerate(unidecode(palavra[0])):
                if lt == resp:
                    resposta.insert(pos, resp)
                    resposta.pop(pos + 1)
                    verificação = True
#Informação dos erros e acertos!!!
            if verificação is False:
                print(f'\033[1;31m{"Letra incorreta!!!":^100}\033[m')
            else:
                print(f'\033[1;33m{"Letra correta!!!":^100}\033[m')
# For da linha 117 Diminui a soma do valor global, já que não deveria descontar tentativas dos acertos.
            for pos, lt in enumerate(unidecode(palavra[0])):
                if lt == resp:
                    if tentativas >= 1:
                        tentativas -= 1
                    break
            for lr in resposta:  # print das palavras corretas na sequencia
                print(f'\033[1;4;32m{lr}\033[m', end=' ')
            print()
            print(f'\033[34mLetras já informadas {letras}\033[m')
            print(f'Dica : \033[1;4;35m{dica}\033[m')
            print('-*-' * 10)
#Saida do Jogo
    elif opção == 4:
        alertas('Saindo do Jogo...Até logo!')
        break
#Caso a opção digitada não for válida
    else:
        print('Opção incorreta. Digite novamente!')
        sleep(1)

#Corrigir numero de tentativas - Resolvido
#Informa se a palavra foi correta