'''Exercício Python 053: Crie um programa que leia uma frase
 qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = str(input('Digite a frase: ').upper())
junto = frase.replace(' ','')
tam = len(junto)
nova = ''
for c in range(tam - 1, -1,-1):
    nova = nova + junto[c]

if nova == junto:
    print('A frase {} é um palindromo'.format(frase))
else:
    print('A frase {} não é um palindromo'.format(frase))



