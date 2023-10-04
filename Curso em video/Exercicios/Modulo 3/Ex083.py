'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
print('-='*30)
print(f'{"VALIDAÇÃO DE EXPRESSÕES":.^60}')
expressao = str(input('Digite sua expressão para validação: '))
count = 0
for e in expressao:
    if e in '()':
        count += 1
if count % 2 == 0:
    print('\033[34mEssa expressão está correta!\033[m')
else:
    print('\033[31mEssa expressão está INcorreta!\033[m')
print('-='*30)



