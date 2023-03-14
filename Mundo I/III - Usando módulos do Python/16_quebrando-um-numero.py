# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

n = float(input('Digite um número: '))
m = float(input('Digite um número: '))

print(f'A porção inteira de {n} é {trunc(n)}')
print(f'A porção inteira de {m} é {int(m)}')



