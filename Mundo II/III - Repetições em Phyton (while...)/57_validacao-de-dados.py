# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    s = str(input('[M] - Masculino\n[F] - Feminino\nDigite seu sexo: ')).upper().strip()[0]
    if s in 'MF':
        break
    else:
        print('Sexo inválido.')