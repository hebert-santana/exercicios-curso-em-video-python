# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número inteiro: '))

fat = 1

print(f'{n}! = ', end='')

while n != 0:
    
    
    if n > 1:
        print(f'{n} x ', end='')
        fat = fat * n
        n -= 1
    elif n == 1:
        print(f'{n} = {fat}')
        n -= 1
    
