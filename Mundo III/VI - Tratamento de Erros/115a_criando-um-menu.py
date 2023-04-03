# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

from ex115 import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 01')
    elif resposta == 2:
        cabecalho('Opção 02')
    elif resposta == 3:
        cabecalho('Opção 03')
        sleep(1)
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mOpção inválida.\033[m')
    sleep(2)        

