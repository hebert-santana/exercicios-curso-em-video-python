# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))

lista_termos = []

while len(lista_termos) != 10:
    lista_termos.append(primeiro_termo)
    print(primeiro_termo, end=' ')
    primeiro_termo += r
    