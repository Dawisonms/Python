import urllib.request

import requests
import PyPDF2
from pandas import read_excel

arquivo = read_excel('Telecom.xlsb') #ler arquivo em excel, que deverá estar na mesma pasta onde o programa for executado e com o mesmo nome.
link = 'https://prosegur.ws360.com.br/idocs_viewer_doc.php?ticket=701d418247a7f97a0fa4bb8171dd2120&tipo_doc=TP_DOCUMENTACAOGERAL&idocs_id=32179082'
acesso = requests.get(link)

for seq, coluna in arquivo.iterrows():
    try:
        requests.get(coluna['link'])

    except:
        print('\033[31mLink não encontrado :)\033[m')
    else:
        print('Link ok!')

