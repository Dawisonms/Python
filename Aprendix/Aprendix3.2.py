from datetime import date, timedelta
from time import time
from requests import get
from pandas import read_excel
from Diversos.lib.arquivo import*


inicio = time() #Inicio contagem do tempo
arquivo = read_excel('Telecom.xlsb')  #ler arquivo em excel, que deverá estar na mesma pasta onde o programa for executado e com o mesmo nome.
count = erros = 0 # Inicio contagem de documentos processado e não processados
log = f'{"Log_Telecom"}_{date.today()}.txt' #Nome do arquivo de saida a ser criado (Log)
criararquivo(log) # Def (biblioteca) que cria um arquivo novo

incluir(log,f'{("-")*12}')
incluir(log,f'LOG de saída')# Cabeçario do arquivo de log (saida)
incluir(log,f'{("-")*12}')

for seq, coluna in arquivo.iterrows(): # Para cada linha, executa a operação abaixo
    count += 1
    try: #Tenta ler o link contido na linha
        link = get(coluna['link'])
        nome = (f'{coluna["nome"]}.pdf')
        get(coluna['link'])
    except: # Exceção caso não consiga ler o link
        print(f'\033[31mLink não encontrado linha {count+1} :)\033[m')
        incluir(log,f'Não foi possível ler o link da linha {count+1} ')
        erros += 1
        continue
    else:
        with open(nome, 'wb') as nome:
            nome.write(link.content)
        incluir(log,f'Linha {count+1} do excel com nome {coluna["nome"]} salvo com sucesso!')
fim = time()
tempo = round((fim - inicio)+0.5) #Arredondamento do tempo
tempo = timedelta(seconds=tempo) # Conversão para formato de h:m:s
totaldocs = count-erros
incluir(log,f'Foram salvos o total de {totaldocs} documentos')
incluir(log,f'Tempo total {tempo} minutos')
incluir(log,f'ATENÇÃO!!!!'
            f'Dependendo da quantidade de arquivos, pode demorar um pouco para aparecerem na pasta onde o executável foi rodado!!')


