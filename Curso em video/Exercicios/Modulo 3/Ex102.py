'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
  indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(a=1, show=False):
    '''

    :param a: Colocar qualquer número que deseja saber seu fatorial.
    :param show: False é default, quando colocado True o programa mostra (show) o resultado completo
    :return: Resultado da multiplicação
    '''
    mult = 1
    if show==True:
        for f in range(a, 1, -1):
            mult *= f
            print(f'{f} x ', end='')
        print(1, end=' ')
        print(f'= {mult}')
    if show == False:
        for f in range(1, a+1):
            mult *= f
        return mult


num = fatorial(5, True)
print(num)
