'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
 perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

maior18 = conth = contm = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    while True:
        if sexo not in 'MmFf':
            sexo = str(input('Sexo [M/F]: '))
        else:
            break
    if sexo in 'Mm':
        conth += 1
    if sexo in 'Ff' and idade < 20:
        contm += 1
    print('~'*30)
    perg = str(input('Deseja incluir mais? [S/N]: ')).strip().upper()[0]
    while True:
        if perg not in 'SsNn':
            perg = str(input('Deseja incluir mais? [S/N]: '))
        else:
            break
    if perg == 'N':
        break
    print('~'*30)
print(f'Maior de 18 anos são {maior18} pessoas \nNo total foram {conth} homens \nAinda temos {contm} mulheres menor que 20 anos.')