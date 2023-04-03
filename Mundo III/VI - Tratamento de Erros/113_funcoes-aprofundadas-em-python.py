# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: digite um número válido.\033[m')
            continue
        else:
            return n


n = leiaInt('Digite um número inteiro: ')
m = leiaFloat('Digite um número: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {m}.')
