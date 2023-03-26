# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

lista = []
dados = []

qnt = int(input('Quantas pessoas deseja adicionar na lista? '))
contador = 0

while contador < qnt:
    nome = str(input('Digiteo nome da pessoa: ')).upper().strip()
    dados.append(nome)
    idade = float(input('Digite o peso da pessoa (Kg): '))
    dados.append(idade)
    lista.append(dados[:])
    dados.clear()
    contador += 1

soma_pesos = 0
for pessoa in lista:
    soma_pesos += pessoa[1]
    
media_pesos = soma_pesos / len(lista)

mais_pesadas = []
menos_pesadas = []
for pessoa in lista:
    if pessoa[1] > media_pesos:
        mais_pesadas.append(pessoa[:])
    else:
        menos_pesadas.append(pessoa[:])
        

print(f'Foram cadastradas {len(lista)} pessoas.')        
print(f'Lista das pessoas mais pesadas: {mais_pesadas}')
print(f'Lista das pessoas menos pesadas: {menos_pesadas}')
    
    
    
        
