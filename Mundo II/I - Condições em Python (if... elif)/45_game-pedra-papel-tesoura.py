# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

print('---------- Bem-vindo ao jogo Jokenpô ----------\n')

opcoes = [1, 2, 3]
computador = choice(opcoes)

if computador == 1:
    computador = 'pedra'
elif computador == 2:
    computador = 'papel'
else:
    computador = 'pedra'

while True:
    print('\nOPÇÕES\n[1] - pedra\n[2] - papel\n[3] - tesoura\n\n')
    jogador = int(input('Digite o número da sua escolha: '))
    if jogador in opcoes:
        if jogador == 1:
            jogador = 'pedra'
        elif jogador == 2:
            jogador = 'papel'
        else:
            jogador = 'pedra'
        break
    else:
        print('Opção inválida.')


print(f"\nVocê escolheu {jogador} e o computador escolheu {computador}.\n")

if jogador == computador:
    print("Empate!")
elif jogador == "pedra":
    if computador == "papel":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
elif jogador == "papel":
    if computador == "tesoura":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
else:
    if computador == "pedra":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
        
print()