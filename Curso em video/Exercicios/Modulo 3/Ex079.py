'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = []
while True:
    num = int(input('Qual valor: '))
    if num in valores:
        print('\033[31mEsse numero já existe, não será incluido...\033[m')
    else:
        valores.append(num)
        print('\033[34mValor incluido com sucesso...\033[m')
    while True:
        print('-=' * 30)
        perg = str(input('Deseja continuar [S/N]: '))
        if perg in 'NnSs':
            break
    print('-='*30)
    if perg in 'Nn':
        break
print(sorted(valores))
print('Fim!')
