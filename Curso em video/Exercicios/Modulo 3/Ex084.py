'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = list()
gpesados = list()
gleves = list()
count = leve = pesado = 0
while True:
    nome = str(input('Nome: ').upper())
    peso = int(input('Peso: '))
    pessoas.append([nome, peso])
    count += 1
    while True:
        perg = str(input('Deseja continuar? [S/N]: ')).upper()
        if perg in 'SsNn':
            break
    if perg in 'Nn':
        break
for seq, p in enumerate(pessoas):
    if seq == 0:
        leve = pesado = p[1]
        gleves.append(p[0])
        gpesados.append(p[0])
    else:
        if leve > p[1]:
            del gleves[:]
            gleves.append(p[0])
            leve = p[1]
        elif leve == p[1]:
            gleves.append(p[0])
        if pesado < p[1]:
            del gpesados[:]
            gpesados.append(p[0])
            pesado = p[1]
        elif pesado == p[1]:
            gpesados.append(p[0])
print(f'Foram cadastradas {count} pessoas')
print(f'A pessoa mais pesada tem {pesado} Kg {gpesados}')
print(f'A pessoa mais leve tem {leve} Kg {gleves}')


