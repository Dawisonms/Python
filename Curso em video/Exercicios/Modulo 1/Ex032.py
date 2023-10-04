#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


#Nota internet Essa regra de adicionar um dia extra a cada quatro anos é uma convenção do calendário gregoriano,
# o calendário civil mais amplamente utilizado atualmente.
# No entanto, existem algumas exceções a essa regra.
# Por exemplo, anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400.
# Isso é feito para manter o alinhamento correto do calendário com o ano solar ao longo do tempo.
from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
        print('\033[31m Esse ano não e bissexto')
    else:
        print('\033[34m Esse ano é bissexto')

else:
    print('\033[31m Esse ano não é bissexto')


