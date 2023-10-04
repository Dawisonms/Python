'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''
print('\033[35m-='*30)
print('Vamos analisar se podemos fazer um triangulo e qual modelo')
r1 = float(input('Primeira medida: '))
r2 = float(input('Segunda medida: '))
r3 = float(input('Terceira medida: '))
print('-='*30)
print('\033[m')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podemos fazer um triangulo:')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 and r2 != r1 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')


else:
    print('Não podemos fazer um triangulo com essas medidas')
