# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

n50 = 0
n20 = 0
n10 = 0
n01 = 0

while True:
    valor = int(input('Valor a ser sacado: '))
    
    # notas de 50
    if valor >= 50:
        n50 = valor // 50
        valor = valor % 50
        print(f'Notas de 50: {n50}')
    
    # notas de 20
    if valor >= 20:
        n20 = valor // 20
        valor = valor % 20
        print(f'Notas de 20: {n20}')
        
    # notas 10
    if valor >= 10:
        n10 = valor // 10
        valor = valor % 10
        print(f'Notas de 10: {n10}')
        
    # notas 1
    if valor < 10:
        n01 = valor
        valor -= n01
        print(f'Notas de 1: {n01}')
        
    if valor == 0:
        break
    
    
    
    
    