# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_gasto = 0
mais_de_1k = 0
mais_barato = ''
menor_preco = None

while True:
    nome = input('Digite o nome do produto: ').upper().strip()
    preco = float(input('Digite o preço do produto R$: '))
    
    total_gasto += preco
    if preco > 1000:
        mais_de_1k += 1
        
    if menor_preco is None or preco < menor_preco:
        menor_preco = preco
        mais_barato = nome
        
    continuar = input('[S] - sim\n[N] - não\n Deseja continuar? ').upper().strip()[0]
    if continuar == 'N':
        break
    
    
print(f'Total gasto: R${total_gasto}')
print(f'{mais_de_1k} produtos custam mais de R$ 1000')
print(f'O produto mais barato é: {mais_barato}')
        
    
            
    