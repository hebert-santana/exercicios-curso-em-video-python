# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from uteis import moedas

v = float(input('Digite um valor: R$ '))

while True:
    op = str(input('[1] - aumentar\n[2] - diminuir\n[3] - dobro\n[4] - metade\nDigite a operação desejada: ')).strip()[0]
    if op == '1':
        v = moedas.aumentar(v)
        print(v)
    elif op == '2':
        v = moedas.diminuir(v)
        print(v)
    elif op == '3':
        v = moedas.dobro(v)
        print(v)
    elif op == '4':
        v = moedas.metade(v)
        print(v)   
    else:
        print('Operação inválida.')
        
    continuar = str(input('[S] - sim\n[N] - não\nDeseja continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break