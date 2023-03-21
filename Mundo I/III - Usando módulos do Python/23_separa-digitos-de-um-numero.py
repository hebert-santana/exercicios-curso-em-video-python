# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

from random import randint

num_aleatorio = randint(0, 9999)
num_aleatorio_str = str(num_aleatorio)
num_digitos = len(num_aleatorio_str)

print(f'Número aleatório: {num_aleatorio}')
print()

if num_digitos == 4:
    print(f'Milhar: {num_aleatorio_str[0]}')
    print(f'Centena: {num_aleatorio_str[1]}')
    print(f'Dezena: {num_aleatorio_str[2]}')
    print(f'Unidade: {num_aleatorio_str[3]}')
elif num_digitos == 3:
    print(f'Centena: {num_aleatorio_str[0]}')
    print(f'Dezena: {num_aleatorio_str[1]}')
    print(f'Unidade: {num_aleatorio_str[2]}')
elif num_digitos == 2:
    print(f'Dezena: {num_aleatorio_str[0]}')
    print(f'Unidade: {num_aleatorio_str[1]}')
else:
    print(f'Unidade: {num_aleatorio_str}')
    
    
    