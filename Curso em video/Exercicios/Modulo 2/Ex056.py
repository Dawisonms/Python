'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
  têm menos de 20 anos.'''
S_idades = 0
maior = 0
mulher = 0
homem = ()

for c in range(1,5):
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M] ou [F]: ')).upper()
    grupo = (nome, idade, sexo)
    print('-'*40) # divide os dados das pessoas
    pessoas = c # conta o numero de pessoas
    S_idades = S_idades + idade # soma as idades
    if idade < 20 and sexo == 'F': # validação mulher menor 20 anos
        mulher = mulher + 1
    if grupo[1] > maior and sexo == 'M': # validação maior idade M
        maior = grupo[1]
        homem = grupo[0]


print('A média de idade desse grupo é de {:.2f} anos'.format(S_idades / pessoas))
if maior > 0:
    print('O homem mais velho desse grupo tem {} anos e seu nome é {}'.format(maior, homem))
else:
    print('Não existem homens nesse grupo')
if mulher >= 1:
    print('{} Mulher(s)  tem menos de 20 anos'.format(mulher))
else:
    print('Não existe mulher com menos de 20 anos nesse grupo')

