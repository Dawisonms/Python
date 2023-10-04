'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

brasileirao =('botafogo', 'gremio', 'flamengo', 'palmeiras', 'bragantino', 'fluminese', 'são paulo', 'internacional', 'atletico PR', 'atletico MG','fortaleza', 'cruzeiro', 'cuiaba', 'santos', 'bahia', 'corinthians', 'goias', 'vasco', 'america MG', 'coritiba')
print('='*150)
print('A classificação do campeonato dia 07/07/2023 é: ')
posicao = primeiros = aleat = 0
ultimos = 16
for time in brasileirao:
    posicao += 1
    print(f'{posicao}º {time}')
print('='*150)
print('OS PRIMEIROS 5 COLOCADOS SÃO:')
for time in brasileirao[:5]:
    primeiros += 1
    print(f'{primeiros}º {time}')
print('='*150)
print('OS ULTIMOS 4 COLOCADOS SÃ0:')
for time in brasileirao[-4:]:
    ultimos += 1
    print(f'{ultimos}º {time}')
print('='*150)
print('OS TIMES EM ORDE ALFABÉTICA SÃO:')
print(sorted((brasileirao)))
print('='*150)
print('A POSIÇÃO DO CORINTHIANS')
for time in brasileirao:
    corinthians = brasileirao.index('corinthians')+1
print(f'A posição do Corinthias é a {corinthians}º')


