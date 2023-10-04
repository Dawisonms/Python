'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
 de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
 o total de gols feitos durante o campeonato.'''
gols = []
total = 0
jogos = {
'jogador': str(input('Nome: ').upper()),
'partidas' : int(input('Quantas partidas jogou: '))}

for p in range(0, jogos['partidas']):
    Ngols = int(input(f'Gols da {p+1}ª partida: '))
    gols.append(Ngols)
    total += Ngols
jogos['Gols'] = gols
jogos['total'] = total
print('-='*30)
print(jogos)
print('-='*30)
for j, p in jogos.items():
    if j != 'partidas':
        print(f'O campo {j} tem o valor {p}')
print('-='*30)
print(f'O jogador {jogos["jogador"]} jogou {jogos["partidas"]} partidas, sedo: ')
for p, g in enumerate(jogos['Gols']):
    print(f'    => Na partida {p+1}, fez {g} gol(s)')
print(f'Foi um total de {jogos["total"]} gols')
print('-='*30)
