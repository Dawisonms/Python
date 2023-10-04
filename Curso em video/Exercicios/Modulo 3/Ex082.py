'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

numeros = []
pares = []
impares = []
while True:
    num = int(input('Qual número: '))
    numeros.append(num)
    while True:
        perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()
        if perg in 'SN':
            break
    if perg in 'N':
        break
    print('~'*40)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Os números digitados foram {numeros}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')
print(f'/033[33m{"FIM":~^80}')