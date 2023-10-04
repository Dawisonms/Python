'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    print('-='*40)
    while True:
        perg = str(input('Deseja continuar? [S/N]')).upper().strip()
        print('-='*40)
        if perg in 'NnSs':
            break
    if perg in 'Nn':
        break
print(f'\033[33m{"Fim":-^80}')
print(f'Foram digitados {len(numeros)} números à sua lista')
print(f'Os numeros digitados de forma decrescentes foram {sorted(numeros,reverse=True)}')
if numeros.count(5) > 0:
    print('O número 5 foi digitado e está na lista')
else:
    print('O número 5 NÃO foi digitado nessa listagem')
print('-='*40)

