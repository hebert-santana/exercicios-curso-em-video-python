# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite a frase: ').upper().strip().replace(' ', '')

frase_invertida = frase[::-1]

if frase == frase_invertida:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')
