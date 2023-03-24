# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print(' ---------- SELECIONE A OPÇÃO DESEJADA ----------')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')

    opcao = int(input('\nQual é a sua opção? '))

    if opcao == 1:
        resultado = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {resultado:.2f}')
    elif opcao == 2:
        resultado = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {resultado:.2f}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'A maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')

print('Fim do programa!')
