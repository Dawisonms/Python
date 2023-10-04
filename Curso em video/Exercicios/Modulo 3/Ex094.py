'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

cadastro = []
pessoas = {}
count = idade = Sidade = media = 0
mulheres = []
acima = []
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: '))
        if sexo in 'MmFf':
            pessoas['sexo'] = sexo
            break
    pessoas['Idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    count += 1
    Sidade += pessoas['Idade']
    media = Sidade / count
    if pessoas['Idade'] >= media:
        acima.append(pessoas.copy()['nome'])
    if pessoas['sexo'] in 'Ff':
        mulheres.append(pessoas.copy()['nome'])
    while True:
        perg = str(input('Deseja continuar [S/N]: '))
        if perg in 'SsNn':
            break
    if perg in 'Nn':
        break
print(f'Foram cadastradas {count} pessoas')
print(f'A média de idade do grupo é {media:.2f} anos')
print(f'A (as) mulheres cadastradas no grupo foram', end=', ')
for m in mulheres:
    print(f'{m}',end=', ')
print()
print(f'As pessoas com idade acima da média são', end=' , ')
for a in acima:
    print(f'{a}', end=', ')
