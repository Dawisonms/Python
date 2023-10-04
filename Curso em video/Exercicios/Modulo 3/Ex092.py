'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
 com quantos anos a pessoa vai se aposentar (35 anos).'''
from datetime import date
cadastro = {
'nome' : str(input('Nome: ')).upper(),
'ano': int(input('Ano de nascimento: ')),
'CTPS': int(input('No CTPS: '))}
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
idade = date.today().year - cadastro['ano']
if cadastro['CTPS'] != 0:
    Ttrabalho = date.today().year - cadastro['contratação']
    aposentadoria = (35 - Ttrabalho) + date.today().year
print('*'*35)
print(f'Nome: {cadastro["nome"]}')
print(f'Idade : {idade} anos')
if cadastro['CTPS'] != 0:
    print(f'CTPS: {cadastro["CTPS"]}')
    print(f'Tempo de trabalho: {Ttrabalho} anos')
    print(f'Aposentadoria prevista: {aposentadoria}')
else:
    print('Sem dados para calculo de trabalho e aposentadoria!')
print('*'*35)
