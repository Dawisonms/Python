'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
  se ele quer ou não continuar a digitar valores.
'''
soma = maior = menor = cont = 0
pergunta = 'S'
while pergunta != 'N':
        num = int(input('Digite um número: '))
        cont += 1
        soma += num
        if cont == 1:
                maior = menor = num
        else:
                if num > maior:
                        maior = num
                if num < menor:
                        menor = num
        pergunta = str(input('Deseja continuar: [S/N]: ')).strip().upper()
media = soma/cont
print('A média dos números digitados foi {:.2f}'.format(media))
print('O maior número é o número {}'.format(maior))
print('O menor número é o número {}'.format(menor))