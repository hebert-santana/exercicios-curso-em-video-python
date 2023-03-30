# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area_terreno = l * c
    print(f'A área do terreno é de {area_terreno} m².')

largura = float(input('Digite a largura do terreno (em metros): '))
comprimento = float(input('Digite o comprimento do terreno (em metros): '))

area(largura, comprimento)
