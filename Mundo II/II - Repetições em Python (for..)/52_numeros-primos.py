# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

while True:
    n = int(input('Digite um número inteiro: '))
    
    if n == 1:
        print('Número não é primo.')
        break
    elif n == 2:
        print('Número é primo.')
        break
    else:
        for i in range(2, n):
            if n % i == 0:
                print('Número não é primo.')
                break
            else:
                print('Número é primo.')
                break