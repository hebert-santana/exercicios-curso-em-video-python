# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

while True:
    computador = randint(0, 10)
    jogador = input('[P] - par\n[I] - impar\nEscolha par ou impar: ').upper().strip()[0]
    if jogador in 'PI':
        jogador_numeros = int(input('Escolha um núméro: '))
        total = jogador_numeros + computador
        print(f'Número: {total}')
        if total % 2 == 0:
            if jogador == 'P':
                print('Você venceu.')
                vitorias += 1
            else:
                print('Você perdeu.')
                break
        else:
            if jogador == 'I':
                print('Você venceu.')
                vitorias += 1
            else:
                print('Você perdeu.')
                break            
    else:
        print('Escolha inválida.')
        
print(f'Número de vitórias: {vitorias}')