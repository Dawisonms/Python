#Bibliotecas usadas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep
import pyautogui as py
import pyperclip


#Comando para 'ativar o serviço se web'
servico = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=servico)


arquivo = pd.read_excel('Telecom.xlsb') #ler arquivo em excel, que deverá estar na mesma pasta onde o programa for executado e com o mesmo nome.

pd.set_option("display.max_colwidth", None) #mostrar todos os itens do link (efeito visual para programação)


chrome #abre o navegador
sleep(20)
for index, row in arquivo.iterrows():#leitura linha a linha da planilha
    print(row["link"] + row["nome"])
    chrome.get(row['link'])#entra no link linha a linha
    sleep(6)
    pyperclip.copy(row["nome"])#copia o nome que será salvo
    py.hotkey('ctrl','s')#para abrir o campo salvar
    sleep(2)
    py.hotkey('ctrl','v')#cola o nome salvo
    sleep(1)
    py.hotkey('enter')#salvar
    sleep(1)

chrome.quit() #depois de executar toda a planilha, fecha o navegador
#Mensagem final
py.alert(text='Fim da Execução', title='Aprendix 2.1', button = 'OK')

# Na versão 2.2 não tem a necessidade de atualizar o webdrive
#
#