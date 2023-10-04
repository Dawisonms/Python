'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
 usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = cont = barato = caro = 0
nome = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Qual preço: R$ '))
    cont += 1
    if cont == 1:
        barato = preço
        nome = produto
    else:
        if preço < barato:
            barato = preço
            nome = produto
    print('~'*30)
    perg = str(input('Deseja incluir mais: [S/N]: ')).strip().upper()[0]
    total += preço
    if preço > 1000:
        caro += 1
    while True:
        if perg not in 'SsNn':
            perg = str(input('Deseja incluir mais produtos! [S/N]: '))
        else:
            break
    if perg in 'Nn':
        break
    print('~'*30)
print('~'*30)
print(f'O tatal gasto foi de R$ {total} \n{caro} produtos custam mais de R$ 1.000,00 \nO produto mais barato é o produto {nome} que custa {barato}')
print('~'*30)
print('Fim!')


