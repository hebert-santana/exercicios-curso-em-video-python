# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Bragantino.


times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Ceará', 'Bragantino', 'Atlético-GO', 'Sport', 'Bahia', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')


print('Os 5 primeiros times são: ', times[:5])
print('Os últimos 4 colocados são: ', times[-4:])
print('Times em ordem alfabética: ', sorted(times))
print('O Bragantino está na posição', times.index('Bragantino') + 1)



