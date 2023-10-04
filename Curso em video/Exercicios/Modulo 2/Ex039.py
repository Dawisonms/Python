'''Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


from datetime import date

nascimento = int(input('Qual seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
alistamento = 18

if idade < alistamento:
    print('\033[34mFaltam {} ano(s) para voce se alistar'.format(alistamento-idade))
elif idade == alistamento:
    print('\033[33m Você tem 18 anos e deverá se alistar imediantamente')
else:
    print('\033[31mJá ultrapassou em {} ano(s) do seu alistamento militar'.format(idade-alistamento))