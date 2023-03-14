# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

h = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))

area = h * l
litros_tinta = area / 2

print(f'Para uma parede de {area} m² é necessário {litros_tinta} litros de tinta.')
