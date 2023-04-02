# Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from uteis import moedas

v = float(input('Digite um valor: R$ '))

while True:
    op = str(input('[1] - aumentar\n[2] - diminuir\n[3] - dobro\n[4] - metade\nDigite a operação desejada: ')).strip()[0]
    if op == '1':
        valor = float(input('Deseja aumentar em quanto? R$ '))
        v = moedas.aumentar(v, valor)
        print(v)
    elif op == '2':
        valor = float(input('Deseja diminuir em quanto? R$ '))
        v = moedas.diminuir(v, valor)
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