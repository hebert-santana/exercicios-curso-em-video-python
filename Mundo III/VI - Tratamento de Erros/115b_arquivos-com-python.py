# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.

from ex115 import *
from ex115arquivo import *
from time import sleep

arq = 'exercicio-115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
    
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 01')
        # opção de listar o conteudo do arquivo
        lerArquivo(arq)
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

