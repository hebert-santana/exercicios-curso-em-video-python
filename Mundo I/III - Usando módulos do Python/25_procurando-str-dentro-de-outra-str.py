# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o nome da pessoa: ').upper().strip())

if 'SILVA' in nome:
    print(f'O nome "{nome}" possui "SILVA".')
else:
    print(f'O nome "{nome}" não possui "SILVA".')