# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
contador = 0

while contador != 5:
    n = float(input('Digite um valor: '))
    lista.append(n)
    contador += 1
    
maior = max(lista)
menor = min(lista)

print(f'A lista gerada é: {lista}')
for i, valor in enumerate(lista):
    if valor == menor:
        print(f'O menor valor é {menor} e está na índice {i}.')
    elif valor == maior:
        print(f'O maior valor é {maior} e está no índice {i}.')