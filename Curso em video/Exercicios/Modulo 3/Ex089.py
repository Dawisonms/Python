'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
alunos = []
media = count = 0
while True:
    alunos.append([str(input('Aluno: ').upper()), float(input('Nota 1: ')), float(input('Nota 2: '))])
    count += 1
    while True:
        perg = str(input('Deseja continuar a inclusão? [S/N]: ')).upper()
        if perg in 'SN':
            break
    if perg in 'N':
        break
print('-='*15)
print(f'{"BOLETIM GERAL":^30}')
print(f'{"Nº":<5} {"ALUNO":<10} {"MÉDIA":<10}')
for No, a in enumerate(alunos):
    media = (a[1] + a[2]) / 2
    print(f'{No:<5} {a[0]:10} {media:<10.2f}')
print('-='*15)
while True:
    detalhe = int(input('Escolha um numero para analisar no detalhe e 999 para encerrar: '))
    print('-='*30)
    if detalhe == 999:
        print('Até logo!!')
        break
    else:
        if detalhe >= len(alunos):
            print('Escolha um número válido!!')
        else:
            print(f'As notas do aluno(a) {alunos[detalhe][0]} são: {alunos[detalhe][1]} e {alunos[detalhe][2]}')
            print('-='*30)


