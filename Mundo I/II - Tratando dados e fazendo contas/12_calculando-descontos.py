# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: R$ '))
desconto = 0.05

p_com_desconto = p - p * desconto

print(f'Preço antes do desconto: R$ {p}')
print(f'Preço após o desconto: R$ {p_com_desconto}')

