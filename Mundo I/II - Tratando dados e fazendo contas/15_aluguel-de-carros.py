# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Kms rodados: '))
d = int(input('Dias alugados: '))

total_a_pagar = d * 60 + 0.15 * km

print(f'Você alugou o carro por {d} dias.')
print(f'Você rodou {km} quilômetros.')
print(f'Valor Total = R$ {total_a_pagar}.')