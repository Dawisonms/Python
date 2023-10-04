def aumentar(p, n, show=False):
    num = (p * n / 100) + p
    if show: # pode referenciar a def moeda ao inves de informar como abaixo
        num = f'R$ {(p * n /100) + p}'
    return num.replace('.',',')


def diminuir(p, n, show=False):
    num = p - (p * n / 100)
    if show:# pode referenciar a def moeda ao inves de informar como abaixo
        num = f'R$ {p - (p * n / 100)}'
    return num.replace('.',',')

def dobro(p, show=False):
    num = p * 2
    if show:# pode referenciar a def moeda ao inves de informar como abaixo
        num = f'R$ {p * 2}'
    return num.replace('.',',')


def metade(p, show=False):
    num = p / 2
    if show:# pode referenciar a def moeda ao inves de informar como abaixo
        num = f'R$ {p / 2}'
    return num.replace('.',',')


def moeda(num, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')



def resumo(p, a, r):
    print('-' * 40)
    print(f'{"RESUMO DOS VALORES":^40}')
    print('-' * 40)
    num = (f'Preço analisado:   R${p}\n'
           f'Dobro do preço :   R${p * 2}\n'
           f'Metado do preço:   R${p / 2}\n'
           f'{a}% de aumento:   R${(p * a / 100) + p}\n'
           f'{r}% de redução:   R${p - (p * r / 100)}')
    print(num)
    print('-'*40)



