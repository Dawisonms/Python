#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Nome de uma cidade: ')

pri = cidade.split()[0]
val = pri in 'SANTO'

print ('Essa cidade {} começa com a palavra SANTO: {}'.format(cidade,val))

