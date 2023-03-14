# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.


var = input('Atribua algo à variável: ')

# algumas informações (afinal, todas é tende ao infinito)
print(f'Tipo primitivo da variável: {type(var)}')
print(f'Só há espaços na variável? {var.isspace()}')
print(f'A variável pode ser convertida em número? {var.isnumeric()}')
print(f'A variável é alfanumérica? {var.isalnum()}')
print(f'A variável está em maiúsculo? {var.isupper()}')
print(f'A variável está em minúsculo? {var.islower()}')
print(f'A variável está capitalizada? {var.istitle()}')