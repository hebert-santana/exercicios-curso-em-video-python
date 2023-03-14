# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

a = float(input('Digite o ângulo: '))

a_radianos = radians(a)
cos_a = cos(a_radianos)
sen_a = sin(a_radianos)
tan_a = tan(a_radianos)

print(f'Ângulo: {a}°')
print(f'Cos({a}) = {round(cos_a, 2)}')
print(f'Sen({a}) = {round(sen_a, 2)}')
print(f'Tan({a}) = {round(tan_a, 2)}')