def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc