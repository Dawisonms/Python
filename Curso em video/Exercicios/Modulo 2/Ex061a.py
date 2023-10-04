'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

primeiro = int(input('Qual o primeiro termo da PA: '))
razão = int(input('Qual a razão dessa PA: '))
termo = primeiro - razão
quant = 10
PA = termo
print('A PA completa é: ')
while quant != 0:
    quant = quant - 1
    PA = PA + razão
    print(PA, end=',')
