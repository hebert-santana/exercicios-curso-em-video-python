# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('\033[33m==================== VALIDA TRIÂNGULO ====================\033[0m')
print("Informe as medidas dos lados do triângulo.")
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

# soma dos lados
soma_ab = a + b
soma_ac = a + c
soma_bc = b + c
somas = [soma_ab, soma_ac, soma_bc]

def validarTriangulo (lado1, lado2, lado3):
    for i in somas:
        if i > lado1 and i > lado2 and i > lado3:
            print('\033[33mTriângulo Validado!\033[0m')
            if lado1 == lado2 and lado2 == lado3:
                print("Triângulo Equilátero: três lados iguais.")
                break
            elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
                print("Triângulo Escaleno: três lados diferentes.")
                break
            else:
                print("Triângulo Isósceles: quaisquer dois lados iguais.")
                break
        else:
            print("\033[31mAs medidas não formam um triângulo válido!\033[0m")
            break
    
validarTriangulo(a, b, c)

print('\033[33m==================== ================ ====================\033[0m')