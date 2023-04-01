# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# Importante: use cores.


from termcolor import colored


def ajuda(comando):
    # Utilizando a função help do Python para obter a documentação do comando
    help(comando)
    # Imprimindo uma mensagem de separação
    print(colored("=" * 50, "blue"))


while True:
    comando = input(colored("Digite um comando (ou FIM para sair): ", "green")).strip().upper()
    if comando == "FIM":
        break
    else:
        # Se não quiser sair, exibindo a documentação do comando digitado
        ajuda(comando)
        # Imprimindo uma mensagem de separação
        print(colored("=" * 50, "blue"))    

# Imprimindo uma mensagem de encerramento
print(colored("Até mais!", "magenta"))
