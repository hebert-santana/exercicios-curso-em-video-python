# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

num_9 = numeros.count(9)

# encontrando a posição do primeiro numero 3 na tupla
pos_3 = None
if 3 in numeros:
    pos_3 = numeros.index(3) + 1

# encontrando os números pares na tupla
pares = tuple(filter(lambda n: n % 2 == 0, numeros))





print(f'O valor 9 apareceu {num_9} vezes.')

if pos_3 != None:
    print(f'O primeiro valor 3 foi digitado na posição {pos_3}.')
else:
    print('Não foi digitado nenhum valor 3.')
    
    
print(f'Os números pares digitados foram: {pares}.')
