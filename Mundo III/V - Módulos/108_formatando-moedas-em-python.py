# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

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

v = moedas.moeda(v)
print(f'O valor final é {v}')