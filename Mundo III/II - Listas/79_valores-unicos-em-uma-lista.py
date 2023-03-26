# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
qnt = int(input('Quantos números deseja adicionar na lista? '))
contador = 0

while contador < qnt:
    n = float(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        contador += 1
    else:
        print('Esse número já foi inserido na lista.')
        
print(f'Lista original: {lista}')

lista.sort()
print(f'Lista em ordem crescente: {lista}')