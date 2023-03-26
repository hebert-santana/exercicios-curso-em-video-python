# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

qnt_jogos = int(input('Quantos jogos serão gerados? '))
cartelas = []

for jogos in range(qnt_jogos):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    cartelas.append(jogo[:])
    jogo.clear()
    
for (jg), cartela in enumerate(cartelas):    
    print(f'Jogo {jg+1}: ', end='')
    for numeros in cartela:
        print(f'{numeros:^3}', end=' ')
    print()
    
