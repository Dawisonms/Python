'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1 + n2 + n3)/ 3
print('Sua média foi {} {:.1f} {}'.format('\033[7m', media, '\033[m'))
if media < 5:
    print('Você está {}REPROVADO'.format('\033[31m'))
elif 5 <= media < 7:
    print('Você ficou em {}RECUPERAÇÃO'.format('\033[33m'))
else:
    print('Parabéns,você foi {}APROVADO'.format('\033[34m'))