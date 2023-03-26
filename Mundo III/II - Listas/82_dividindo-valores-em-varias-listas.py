# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
qnt = int(input('Quantos números deseja adicionar na lista? '))
contador = 0

while contador < qnt:
    n = float(input('Digite um número: '))
    lista.append(n)
    contador += 1
        
lista_par = []
lista_impar = []

for num in lista:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
        
print(f'Lista original: {lista}')
print(f'Lista par: {lista_par}')
print(f'Lista impar: {lista_impar}')