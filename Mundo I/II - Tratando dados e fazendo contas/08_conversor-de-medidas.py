# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite a medida em metros: '))

cm = metros * 100
mm = cm * 100

print(f'{metros} metros = {cm} centímetros = {mm} milímetros')