# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
quantidade = 0

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    else:
        soma += n
        quantidade += 1
        

print(f'A soma dos números digitados é: {soma}')
print(f'A quantidade de números digitados foi: {quantidade}')