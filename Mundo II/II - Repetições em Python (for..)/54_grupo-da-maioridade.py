# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = 2023 - ano_nascimento
    
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} pessoas são maiores de idade.')
print(f'{menores} pessoas são menores de idade.')
