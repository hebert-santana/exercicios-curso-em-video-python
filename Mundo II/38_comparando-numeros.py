# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

maior = n1

if n2 == maior:
    print('Não existe valor maior, os dois são iguais.')
elif n2 > maior:
    print('O segundo valor é maior.')
else:
    print('O primeiro valor é maior.')
    

