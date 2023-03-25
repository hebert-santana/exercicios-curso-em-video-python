# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
lista_numeros = []

while True:
    n = int(input('Digite um número inteiro: '))
    soma += n
    lista_numeros.append(n)
    continua = (input('[S] - sim\n[N] - não\nDeseja inserir mais números? ')).upper().strip()[0]
    if continua == 'N':
        break
    elif continua != 'S':
        print('Valor inválido! Contina por padrão.')

media = soma / len(lista_numeros)

lista_numeros.sort()
maior = lista_numeros[-1]
menor = lista_numeros[0]
        

print(f'A media dos números digitados é: {media:.2f}')
print(f'Maior valor: {maior}\nMenor valor: {menor}')