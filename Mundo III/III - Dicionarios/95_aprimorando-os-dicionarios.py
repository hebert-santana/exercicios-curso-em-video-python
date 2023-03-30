# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from tabulate import tabulate

lista_jogadores = []
jogador = {}

while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: ')).strip().title()
    jogador['Partidas'] = int(input('Digite o número de partidas disputadas: '))
    gols = 0
    for partida in range(1, jogador['Partidas']+1):
        gols += int(input(f'Digite o número de gols marcados na partida {partida}: '))
    jogador['Gols'] = gols
    jogador['Gols/Partida'] = round(gols/jogador['Partidas'], 2)
    lista_jogadores.append(jogador.copy())
    
    continuar = str(input('\n\n[S] - sim\n[N] - não\nDeseja cadastrar outro jogador? ')).strip().upper()[0]
    if continuar == 'N':
        break
    else:
        continue
    
print(lista_jogadores)


# Transforma a lista de dicionários em uma lista de listas
lista_tabela = [[jogador['Nome'], jogador['Partidas'], jogador['Gols'], jogador['Gols/Partida']] for jogador in lista_jogadores]

# Imprime a tabela usando a biblioteca tabulate
print(tabulate(lista_tabela, headers=['Nome', 'Partidas', 'Gols', 'Gols/Partida']))
