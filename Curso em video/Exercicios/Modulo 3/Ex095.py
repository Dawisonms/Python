'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
 de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
 o total de gols feitos durante o campeonato.'''
jogadores =[]
gols = []
jogos = {}
while True:
    jogos['jogador'] = str(input('Nome: ').upper())
    jogos['partidas'] = int(input('Quantas partidas jogou: '))
    for p in range(0, jogos['partidas']):
        Ngols = int(input(f'Gols da {p+1}ª partida: '))
        gols.append(Ngols)
        jogos['Gols'] = gols.copy()
    jogos['total'] = sum(gols)
    jogadores.append((jogos.copy()))
    jogos.clear()
    gols.clear()
    while True:
        perg = str(input('Quer continuar? [S/N]: '))
        if perg in 'SsNn':
            break
    if perg in 'Nn':
        break
print('-='*30)
print(f'{"cod":<3} {"nome":<12} {"Gols":<15} {"Total":<20}')
while True:
    for pos, j in enumerate(jogadores):
       print(f'{pos + 1:<3} {j["jogador"]:<12} {str(j["Gols"]):<15} {j["total"]:<20}')
    while True:
        print('-='*30)
        dados = int(input('Quer mostrar os dados de qual jogador? '))
        for pos, j in enumerate(jogadores):
            if dados == pos + 1:
                print(f'--Levantamento do jogador -- {j["jogador"]}')
                for p in range(j['partidas']):
                    print(f'Na partida {p + 1} fez {j["Gols"][p]} gol(s)')
        if dados == 999:
            break
    if dados == 999:
        print('Até breve!!')
        break






