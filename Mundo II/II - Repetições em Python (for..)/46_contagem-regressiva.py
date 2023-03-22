# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
# importar pacote para gerar arte no print de "feliz ano novo"
from art import *

for i in range(10, 0, -1):
    print(i)
    sleep(0.1)

print()    
Art=text2art("FELIZ   ANO   NOVO")
print(Art)
