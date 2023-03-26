# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

qnt = 1
lista = []
lista_par = []
lista_impar = []

while qnt < 8:
    n = int(input(f'Digite o {qnt}o. número inteiro: '))
    
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
        
    qnt += 1
    
lista_par.sort()
lista_impar.sort()

lista.append(lista_par[:])
lista.append(lista_impar[:])

print(lista)
    