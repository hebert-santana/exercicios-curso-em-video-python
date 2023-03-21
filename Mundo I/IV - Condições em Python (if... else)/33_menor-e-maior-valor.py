# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

menor = n1
maior = n1

if n2 > maior:
    maior = n2
    
if n3 > maior:
    maior = n3


if n2 < menor:
    menor = n2
    
if n3 < menor:
    menor = n3
    

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')
