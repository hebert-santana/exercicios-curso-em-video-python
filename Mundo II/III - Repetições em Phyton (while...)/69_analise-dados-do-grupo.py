# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mulheres_menor_20 = 0
homens = 0
maior_18 = 0

while True:
    sexo = input('[M] - masculino\n[F] - feminino\nInforme o sexo da pessoa: ').upper().strip()[0]
    if sexo in 'MF':
        idade = int(input('Digite a idade da pessoa: '))
        
        if sexo == 'M':
            homens += 1
        else:
            if idade < 20:
                mulheres_menor_20 += 1
            
        
        if idade > 18:
            maior_18 += 1
            
        continuar = input('[S] - sim\n[N] - não\n Deseja continuar? ').upper().strip()[0]
        if continuar == 'N':
            break
        
        
    else:
        print('Sexo inválido')
        

print(f'Pessoas com mais de 18 anos: {maior_18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menor de 20 anos: {mulheres_menor_20}')