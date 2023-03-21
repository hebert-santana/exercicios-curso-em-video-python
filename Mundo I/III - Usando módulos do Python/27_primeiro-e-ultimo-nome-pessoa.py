# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ').upper().strip())

lista_nome_separado = nome.split()

primeiro_nome = lista_nome_separado[0]
ultimo_nome = lista_nome_separado[-1]

print(f'Primeiro nome: {primeiro_nome}.')
print(f'Último nome: {ultimo_nome}.')