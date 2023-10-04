''' Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será
 a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Digite um numero para converção: '))
print(''''Escolha uma opção abaixo para converção:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opção = int(input('sua opção: '))

if opção == 1:
    print('O número {} convertido em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} onvertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção incorreta, tente outra vez!')
