# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
# a) de 1 até 10, de 1 em 1                                                                                                                                              
# b) de 10 até 0, de 2 em 2                                                                                                                                            
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
        
    if inicio < fim:        
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM!')
        
    else:
        for i in range(inicio, fim-1, -passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM!')

# a) contagem de 1 até 10, de 1 em 1
print('a) Contagem de 1 até 10, de 1 em 1:')
contador(1, 10, 1)

# b) contagem de 10 até 0, de 2 em 2
print('\nb) Contagem de 10 até 0, de 2 em 2:')
contador(10, 0, 2)

# c) contagem personalizada
print('\nc) Contagem personalizada:')
inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor de fim: '))
passo = int(input('Digite o valor do passo: '))
contador(inicio, fim, passo)
