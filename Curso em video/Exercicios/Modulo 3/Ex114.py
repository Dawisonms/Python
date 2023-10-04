'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mSite Pudim não encontrado :)\033[m')
else:
    print('\033[33mSite Pudim encontrado com sucesso!!!\033[m')
    print(site.read())


