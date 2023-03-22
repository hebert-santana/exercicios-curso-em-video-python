# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 
# 2 para octal e 
# 3 para hexadecimal.

n = int(input('Digite um número: '))
c = int(input('[1] para binário\n[2] para octal\n[3] para hexadecimal\nEscolha a conversão: '))

binario = bin(n)[2:]
octal = oct(n)[2:]
hexadecimal = hex(n)[2:]

if c == 1:
    print(f'{n} em binario = {binario}')
elif c == 2:
    print(f'{n} em octal = {octal}')
elif c == 3:
    print(f'{n} em hexadecimal = {hexadecimal}')
else:
    print('Valor inválido.')