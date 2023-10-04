#Bibliotecas usadas
from selenium import webdriver
import pandas as pd
from time import sleep
import pyautogui as py
import pyperclip

#ler arquivo em excel
arquivo = pd.read_excel('Telecom.xlsb')
#Arquivo executavel do Edge
edge = webdriver.Edge(executable_path='msedgedriver.exe')
#mostrar todos os itens do link (efeito visual para programação)
pd.set_option("display.max_colwidth", None)


edge #abre o navegador
sleep(20)
for index, row in arquivo.iterrows():#leitura linha a linha da planilha
    print(row["link"] + row["nome"])
    edge.get(row['link'])#entra no link linha a linha
    sleep(6)
    pyperclip.copy(row["nome"])#copia o nome que será salvo
    py.hotkey('ctrl','s')#para abrir o campo salvar
    sleep(2)
    py.hotkey('ctrl','v')#cola o nome salvo
    sleep(1)
    py.hotkey('enter')#salvar
    sleep(1)

edge.quit() #depois de executar toda a planilha, fecha o navegador
#Mensagem final
py.alert(text='Fim da Execução', title='Aprendix 2.1', button = 'OK')

