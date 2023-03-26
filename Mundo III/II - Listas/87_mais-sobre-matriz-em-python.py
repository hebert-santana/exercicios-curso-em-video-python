# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                               
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0
maior_segunda_linha = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor da posição [{i}][{j}]: '))


print("Matriz 3x3:")
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^7}', end="") # formatando com 7 espaços centralizado
    print() # salta uma linha
    
# somando todos os pares
for n in matriz: # listas na matriz
    for m in n: # elementos nas listas
        if m % 2 == 0:
            soma_pares += m
            
# somando elementos da terceira coluna
for n in matriz:
    if n[2]:
        soma_coluna3 += n[2]
        
# maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

print(f'Soma dos valores pares na matriz: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_coluna3}')
print(f'Maior valor da segunda linha da matriz: {maior_segunda_linha}')
            