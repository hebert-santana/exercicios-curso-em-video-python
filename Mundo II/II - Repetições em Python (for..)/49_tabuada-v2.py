# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

while True:
    n = int(input('Escolha um número entre 0 e 9: '))
    if n >= 0 and n < 10:
        break
    else:
        print('Valor inválido.')

print(f'\nTABUADA DO {n}\n')        
for i in range(0, 10):
    resultado = i * n
    print(f'{i} x {n} = {resultado}')