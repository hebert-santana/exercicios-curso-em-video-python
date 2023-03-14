# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print(f'==================== CONVERTE REAIS EM DÓLARES ====================')
# API para ver a cotação do dólar
import requests
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
# print(cotacoes)
cotacao_dolar = cotacoes['USDBRL']['bid']
print(f'Cotação atual do Dólar = R${cotacao_dolar}')

cotacao_dolar = float(cotacao_dolar)

reais = float(input('Quantos reais você tem: '))
dolar = reais/cotacao_dolar

print(f'Com R${reais} você pode comprar {dolar} dólares.')

