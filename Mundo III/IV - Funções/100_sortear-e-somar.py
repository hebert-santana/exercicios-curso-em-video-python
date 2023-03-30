# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia():
    numeros = []
    for i in range(5):
        numeros.append(randint(1, 10))
    print(f"Numeros sorteados: {numeros}")
    return numeros

def somaPar(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f"Soma dos números pares: {soma}")


numeros_sorteados = sorteia()
somaPar(numeros_sorteados)
