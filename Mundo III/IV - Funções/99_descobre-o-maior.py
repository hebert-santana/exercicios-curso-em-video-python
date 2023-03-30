# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*numeros):
    if len(numeros) == 0:
        print("Não foi informado nenhum valor")
    else:
        maior = numeros[0]
        for numero in numeros:
            if numero > maior:
                maior = numero
        print(f"O maior valor informado foi {maior}.")

# testando a função
maior(1, 3, 5, 7, 9)
maior(-10, 10, 0, 20, 30, -5, 15)
maior(1)
maior()
