'''Adicione ao modulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostra na tela algumas informações
geradas pelas funções que já temos no modulo criadas até aqui'''

from ex111.utilidadescev import moeda

valor = float(input('Digite um valor: '))
moeda.resumo(valor,80, 35)