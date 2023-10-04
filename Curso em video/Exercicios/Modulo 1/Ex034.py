#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual seu salário atual: '))

if salario <= 1250.00:
    print('\033[32m Seu novo salário é {:.2f}'.format(salario + (salario * 0.15)))
else:
    print('\033[35m Seu novo salário é {:.2f}'.format(salario + (salario * 0.10)))