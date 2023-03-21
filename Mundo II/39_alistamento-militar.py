# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o ano do seu nascimento: '))
ano_atual = 2023
idade = 2023 - ano

tempo_falta = 18 - idade
tempo_passou = idade - 18

if idade == 18:
    print('Você deve se alistar neste ano.')
elif idade < 18:
    print(f'Você se alistará no futuro. Faltam {tempo_falta} anos.')
else:
    print(f'Já passou do seu tempo de alistamento. Passou {tempo_passou} anos.')