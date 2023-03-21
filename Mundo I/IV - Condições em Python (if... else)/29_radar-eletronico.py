# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Velocidade (Km/h) = '))
limite = 80

if v > limite:
    print(f'Sua velocidade: {v} Km/h.\nVocê foi multado.')
    diferenca = v - limite
    multa = diferenca * 7
    print(f'Sua multa é: R${multa}.')