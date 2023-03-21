# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite a frase: ').lower().strip())

indice = 0
posicoes = []

for letra in frase:
    if letra == 'a':
        posicoes.append(indice)
    indice += 1
    
primeira_ocorrencia = posicoes[0]
ultima_ocorrencia = posicoes[-1]
numero_ocorrencias = len(posicoes)

print(f'A primeira ocorrência foi no índice: {primeira_ocorrencia}.')
print(f'A última ocorrência foi no índice: {ultima_ocorrencia}.')
print(f'O número de ocorrências foi: {numero_ocorrencias}.')

# opção alternativa
# frase.count('a')
# frase.find('a')
# frase.rfind('a')

