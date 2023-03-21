# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = float(input('Distância da viagem (Km): '))
preco_km = 0.5

if d <= 200:
    preco_total = preco_km * d
else:
    preco_km = 0.45
    preco_total = preco_km * d
    
print(f'Preço total da viagem: R$ {preco_total}')