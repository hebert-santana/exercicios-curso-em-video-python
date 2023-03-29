# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter


resultados = {}

# loop para cada jogador jogar o dado
for jogador in range(1, 5):
    resultado = randint(1, 6)
    resultados[f"Jogador {jogador}"] = resultado
    
ordenado = []
ordenado = sorted(resultados.items(), key=itemgetter(1), reverse=True)    

for i, player in enumerate(ordenado):
    print(f'{i+1}: {player[0]} com {player[1]} pontos.')


    