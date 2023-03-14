# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

alunos = ["Ronaldinho", "Raffa Moreira", "Zidane", "Jovem Nerd"]

aluno_sorteado = random.choice(alunos)

print(f'O aluno sorteado é: {aluno_sorteado}.')





