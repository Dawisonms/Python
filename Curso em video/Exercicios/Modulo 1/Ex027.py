# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome separadamente.


nome = input('Digite seu nome: ')

sobrenome = len(nome.split())

Pnome = nome.split()[0]
Unome = nome.split()[sobrenome-1]
nome2 = Pnome + ' ' + Unome
print('Boa tarde, Sr (a) {}'. format(nome2))

