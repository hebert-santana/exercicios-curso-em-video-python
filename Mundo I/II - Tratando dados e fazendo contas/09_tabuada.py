# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))

print(f'==================== TABUADA DO {n} ====================')

for i in range(0, 10):
    produto = n * i
    print(f'{n} x {i} = {produto}')