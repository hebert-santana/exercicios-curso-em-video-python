# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Escolha um número inteiro: '))
    if n < 0:
        print('Saindo do programa...')
        break
    else:
        print(f'\nTABUADA DO {n}\n')        
        for i in range(0, 10):
            resultado = i * n
            print(f'{i} x {n} = {resultado}')
        print('\n\n')

