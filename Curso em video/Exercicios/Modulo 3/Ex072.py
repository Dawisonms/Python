'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero =int(input('Escolha um numero entre 0 e 20: '))
    if numero < 0 or numero > 20:
        numero = int(input('Escolha um numero entre 0 e 20: '))
    else:
        print(f'O número {numero} por extenso é {extenso[numero]}.')
        print('-' *50)
        while True:
            perg = str(input('Deseja continuar [S/N]: '))
            if perg in 'SsNn':
                break
        if perg in 'Nn':
            break



