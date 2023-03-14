# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
from math import sqrt, pow

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

h = sqrt(pow(ca, 2) + pow(co, 2)) # ou h = hypot(co, ca)

print(f'A hipotenusa é: {h}')
