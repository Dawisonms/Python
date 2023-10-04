from Forca.bibliotecas.config import *
from unidecode import unidecode
from time import sleep
palavras = 'dados.txt'

n_palavra = leiastr('Palavra: ').upper().strip()
with open(palavras, 'r') as a:
    for seq in a:
        n_p = seq.split(';')
        n_p = n_p[0]
        if n_p == n_palavra:
            n_p = True
            break
    if n_p is True:
        print('Palavra já existe')
    else:
        print('Pode cadastrar')



