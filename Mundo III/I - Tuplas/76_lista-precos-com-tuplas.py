# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
from prettytable import PrettyTable

# cria a tabela
x = PrettyTable(['Nome do Time', 'Preço (Milhões)'])
# alinha as colunas
x.align['Nome do Time'] = "l"
x.align['Preço (Milhões)'] = "r"
# deixa um espaço entre a borda das colunas e o conteúdo (default)
x.padding_width = 1

safs = ['Botafogo', 500.00, 'Atlético', 900.00, 'Fluminense', 600.00, 'Vasco', 300.00]

# adiciona cada SAF à tabela
for i in range(0, len(safs), 2):
    x.add_row([safs[i], safs[i+1]])


print(x)

