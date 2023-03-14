# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite o número: '))
antecessor = n - 1
sucessor = n + 1
print(f'O antecessor de {n} é {antecessor}.')
print(f'O sucessor de {n} é {sucessor}.')
