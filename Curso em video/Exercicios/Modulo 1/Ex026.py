#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A",
# em que posição ela aparece
# a primeira vez e em que posição ela aparece
# a última vez.

frase = input('Digite uma frase: ').lower().strip() # No meu código criei uma frase 2, porém pode usar ao final da frase (lower,upper, strip...)
frase2 = frase.strip()
print('Em "{}" :'.format(frase2))

# mostre quantas vezes aparece a letra "A",
print('A letra "A" aparece {} vezes'.format(frase2.count('a')+1))

# em que posição ela aparece


# a primeira vez e em que posição ela aparece
print('A primeira letra "A" aparece na posição numero {}'.format(frase2.find('a')+1))

# a última vez.
print('A ultima vez que a letra "A" aparece é na posição {}'.format(frase2.rfind('a')+1))