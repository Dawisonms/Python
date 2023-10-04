'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = list()
pares = ter = seg = 0
for m in range(0, 3):
    for n in range(0, 3):
        num = int(input(f'Dig o valor para {m, n}: '))
        matriz.append([num])
        if n == 2:
            ter += num
        if num % 2 == 0:
            pares += num
        if m == 2:
            if num > seg:
                seg = num
print(f'{matriz[0]}{matriz[1]}{matriz[2]}')
print(f'{matriz[3]}{matriz[4]}{matriz[5]}')
print(f'{matriz[6]}{matriz[7]}{matriz[8]}')
print(f'A soma dos numeros pares são: {pares}')
print(f'A soma da terceira coluna é: {ter}')
print(f'O maior valor da segunda linha: {seg}')
