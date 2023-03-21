# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

n = randint(0, 5)

while True:
    n_usuario = int(input('Digite um número entre 0 e 5: '))
    if n_usuario >= 0 and n_usuario <= 5:
        if n == n_usuario:
            print('Venceu')
            break
        else:
            print(f'Perdeu, o número era {n}')
            break
    else:
        print('Número Inválido.')
    
