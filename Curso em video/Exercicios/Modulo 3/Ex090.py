'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
 guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = {'nome': str(input("Nome: ")), 'media': float(input("Média: "))}
situação = ''
if aluno['media'] >= 7:
    situação = 'Aprovado'
elif aluno['media'] < 5:
    situação = 'Reprovado'
else:
    situação = 'Em recuperação'

print(situação)