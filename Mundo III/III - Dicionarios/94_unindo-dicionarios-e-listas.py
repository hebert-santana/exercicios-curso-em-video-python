# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoa = {}
lista_pessoas = []

for c in range(3):
    pessoa['Nome'] = input('Nome: ').title().strip()
    pessoa['Sexo'] = str(input('[M] - masculino\n[F] - feminino\nSexo: ')).upper().strip()[0]
    pessoa['Idade'] = int(input('Idade: '))
    lista_pessoas.append(pessoa.copy())
    

# a
pessoas_cadastradas = len(lista_pessoas)

# b
idades = 0
for c in lista_pessoas:
    idades += c['Idade']
media_idades = round(idades / pessoas_cadastradas, 2)

# c
lista_mulheres = []
for p in lista_pessoas:
    if p['Sexo'] == 'F':
        lista_mulheres.append(p.copy())

# d
lista_mais_velhos = []
for p in lista_pessoas:
    if p['Idade'] > media_idades:
        lista_mais_velhos.append(p.copy())
        

print(f'Quantidade de pessoas cadastradas: {pessoas_cadastradas}')
print(f'Média de idade: {media_idades} anos')
print(f'Lista das mulheres: {lista_mulheres}')
print(f'Lista acima da idade média: {lista_mais_velhos}')