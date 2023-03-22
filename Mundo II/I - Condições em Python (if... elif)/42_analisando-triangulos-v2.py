# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        tipo = "EQUILÁTERO"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"
    print(f"É possível formar um triângulo {tipo}.")
else:
    print("Não é possível formar um triângulo com esses valores de lado.")
