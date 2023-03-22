# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Os números pares ente 1 e 50 são: ', end = ' ')

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
