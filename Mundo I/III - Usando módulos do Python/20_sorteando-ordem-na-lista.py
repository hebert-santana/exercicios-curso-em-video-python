# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ["Ronaldinho", "Raffa Moreira", "Zidane", "Jovem Nerd"]
apresentacao = []
ordem = 1

while len(apresentacao) != len(alunos): 
    aluno_sorteado = random.choice(alunos)
    if aluno_sorteado not in apresentacao:
        apresentacao.append(aluno_sorteado)
        print(f'{ordem} - {aluno_sorteado}')
        ordem += 1