# Algoritimo leia o salário e mostre o novo salário com aumento de 15%.

salario = float(input('Salario atual: '))
Aumento = 15
N_salario: float = salario + (salario*15/100)
print('Seu novo salário é {}'.format(N_salario))