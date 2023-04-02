def aumentar(n, v=1):
    return n + v
    
def diminuir(n, v=1):
    return n - v
    
def dobro(n):
    return n*2
    
def metade(n):
    return n/2

def moeda(n, moeda = 'R$'):
    n = f'{moeda}{n:>8.2f}'.replace('.', ',')
    return n

def resumo(n=0):
    print('-' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-' *30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro(n))}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print('-' *30)


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro: \"{entrada}" não é um preço válido.')
        else:
            valido = True
            return float(entrada)