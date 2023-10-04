'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
num1 = float(input('1º valor: '))
num2 = float(input('2º valor: '))
print('''O que você deseja fazer? \033[33m 
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa\033[m''')
opcao = int(input('Opção: '))
while opcao != 5:
    if opcao == 1:
        print('A soma de {} e {},totaliza {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicação de {} por {} é {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 == num2:
            print('Os numeros {} e {},são iguais'. format(num1, num2))
        elif num1 > num2:
            print('O número {} é maior que o número {}'.format(num1, num2))
        else:
            print('O número {} é maior que o número {}'.format(num2, num1))
    elif opcao == 4:
        num1 = int(input('1º valor novo: '))
        num2 = int(input('2º valor novo: '))
    else:
        print('Opção incorreta')
    opcao = int(input('Opção:'))

print('Fim do programa')



