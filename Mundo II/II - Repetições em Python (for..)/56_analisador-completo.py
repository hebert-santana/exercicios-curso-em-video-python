# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homens = []
mulheres = []
soma_idades = 0

for i in range(1, 5):
    nome = input(f'Digite o nome da {i}ª pessoa: ')
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    sexo = input(f'Digite o sexo da {i}ª pessoa (M/F): ').upper()
    pessoa = [nome, idade, sexo]
    soma_idades += idade
    if sexo == 'F':
        mulheres.append(pessoa)
    elif sexo == 'M':
        homens.append(pessoa)



# média das idades do grupo
media_idades = soma_idades / 4
print(f'Idade média do grupo: {media_idades}')

# maior idade entre os homens
maior_idade = 0

for pessoa in homens:
    if pessoa[1] > maior_idade:
        maior_idade = pessoa[1]

for pessoa in homens:
    if pessoa[1] == maior_idade:
        print(f'O homem mais velho é o {pessoa[0]} que tem {maior_idade} anos.')
                

# mulheres com menos de 20 anos
contador = 0                
for pessoa in mulheres:
    if pessoa[1] < 20:
        contador += 1
        
print(f'Há {contador} mulheres com menos de 20 anos.')
                


                
