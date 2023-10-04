import time
from requests import get
from pandas import read_excel

inicio = time.time()
arquivo = read_excel('Telecom.xlsb')  #ler arquivo em excel, que deverá estar na mesma pasta onde o programa for executado e com o mesmo nome.
count = 0
for seq, coluna in arquivo.iterrows():
    link = get(coluna['link'])
    nome = (f'{coluna["nome"]}.pdf')
    count += 1
    try:
        get(coluna['link'])
    except:
        print('\033[31mLink não encontrado :)\033[m')
        continue
    else:
        with open(nome, 'wb') as nome:
            nome.write(link.content)
    print(f'Linha {count + 1} do excel com nome {coluna["nome"]} salvo com sucesso!')
print(f'Foram salvos {count} arquivos!')
fim = time.time()
tempo = fim - inicio
print(f'Tempo total {tempo:.2f} segundos')

