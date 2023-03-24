# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

qnt_termos = 10

termo = int(input('Digite o termo inicial da PA: '))
r = int(input('Digite a razão da PA: '))

print('Progressão Aritmética: ', end='')
while qnt_termos != 0:
    print(termo, end= ' ')
    termo += r
    qnt_termos -= 1