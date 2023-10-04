'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from ex111.utilidadescev import moeda

valor = float(input('Digite um valor: '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor,True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Diminuindo 20% temos {moeda.diminuir(valor, 20, True)}')


