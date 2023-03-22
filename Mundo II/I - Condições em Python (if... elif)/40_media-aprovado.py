# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

while True:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    if n1 >= 0 and n1 <= 10:
        if n2 >= 0 and n2 <= 10:
            break
        else:
            print('Nota inválida.')
    else:
        print('Nota inválida.')
        
media = lambda x, y: (x+y)/2
media_aluno = media(n1, n2)

if media_aluno >= 7:
    print(f'Média {media_aluno}: APROVADO')
elif media_aluno >= 5 and media_aluno < 7:
    print(f'Média {media_aluno}: RRECUPERAÇÃO')
else:
    print(f'Média {media_aluno}: REPROVADO')