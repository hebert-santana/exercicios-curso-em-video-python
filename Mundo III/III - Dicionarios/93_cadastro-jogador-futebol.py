# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}

jogador['Nome'] = str(input('Digite o nome do jogador: ')).strip().title()
jogador['Partidas'] = int(input('Digite o número de partidas disputadas: '))

gols = 0
for partida in range(1, jogador['Partidas']+1):
    gols += int(input(f'Digite o número de gols marcados na partida {partida}: '))

jogador['Gols'] = gols
    
print(jogador)
    