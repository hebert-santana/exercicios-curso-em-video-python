# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []

while True:
    nome = input('Digite o nome do aluno (ou "SAIR" para encerrar): ').upper().strip()
    if nome == 'SAIR':
        break    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    
    lista_alunos.append([nome, nota1, nota2])
    


print("\n==================== BOLETIM ====================")

for aluno in lista_alunos:
    media = (aluno[1] + aluno[2]) / 2
    print(f'{aluno[0]}: Média {media} pts')

print("==================== ======= ====================")

while True:
    escolha = input('\nDigite o nome do aluno para ver as notas (ou "SAIR" para encerrar): ').strip().upper()
    if escolha == 'SAIR':
        break
    
    existe_aluno = False
    for aluno in lista_alunos:
        if aluno[0] == escolha:
            existe_aluno = True
            print(f"Notas do aluno {aluno[0]}:\nPrimeira nota: {aluno[1]}\nSegunda nota: {aluno[2]}")
            break
    
    if not existe_aluno:
        print("Aluno não existe_aluno.")

    
