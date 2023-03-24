# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.


pesos = []

for i in range(1, 6):
    peso = int(input(f'Digite o peso da {i}ª pessoa: '))
    pesos.append(peso)


menor = pesos[0]
maior = pesos[0] 

for i in pesos:
    if i < menor:
        menor = i
    else:
        maior = i
        
print('Pesos: ', end = '')
for i in pesos:
    print(i, end = ' ')
    
print()
print(f'Menor: {menor}\nMaior: {maior}')
