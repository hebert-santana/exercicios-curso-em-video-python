# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor da posição [{i}][{j}]: '))


print("Matriz 3x3:")
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^7}', end="") # formatando com 7 espaços centralizado
    print() # salta uma linha
