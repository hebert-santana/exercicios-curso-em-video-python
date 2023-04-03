# Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.

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
        # opção cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Opção 03')
        sleep(1)
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mOpção inválida.\033[m')
    sleep(2)        
