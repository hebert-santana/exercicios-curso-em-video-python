# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

n = randint(0, 10)

contador = 0
while True:
    palpite = int(input('Digite um palpite: '))
    contador += 1
    if palpite < n:
        print('Palpite baixo.')
    elif palpite > n:
        print('Palpite alto.')
    else:
        print('Acertou.')
        break
    
print(f'Número de palpites até acertar: {contador}')