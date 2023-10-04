#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo: '))

#- O nome com todas as letras maiúsculas e minúsculas.
print(nome.upper())
print(nome.lower())

#- Quantas letras ao todo (sem considerar espaços).
print('Esse nome todo tem {} letras'.format(len(nome.replace(' ',''))))

#- Quantas letras tem o primeiro nome
nome2 = nome.split()
print('O primeiro nome tem {} letras'.format(len(nome2[0])))
