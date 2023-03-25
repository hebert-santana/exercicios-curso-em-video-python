# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 1 – 1 – 2 – 3 – 5 – 8
n = int(input('Digite um número inteiro: '))
limite = n

# termo (n-1)
n1 = 0
# termo (n-2)
n2 = 0
# termo atual da sequência
termo_atual = 0

while termo_atual < n:
    if n1 + n2 > 0:  
        termo_atual = n1 + n2
        n2 = n1
        n1 = termo_atual
    else:
        n1 += 1
        termo_atual = 1
    print(termo_atual, end=' ')
        
