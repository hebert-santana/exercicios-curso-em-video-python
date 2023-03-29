# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dicionario = {}

dicionario['Nome'] = str(input('Digite o nome: ')).capitalize().strip()
dicionario['Média'] = float(input('Digite a média: '))

print(dicionario)


