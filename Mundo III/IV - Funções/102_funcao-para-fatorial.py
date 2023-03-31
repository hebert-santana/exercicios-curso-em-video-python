# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial do número num.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(f'{i} x ' if i > 1 else f'{i} = ', end='')
    return f


num = int(input('Para qual número deseja calcular o fatorial? '))
opcional = input('\n[S] - sim\n[N] - não\nDeseja exibir o cálculo? ').strip().upper()[0]

if opcional == 'S':
    valor_logico = True
else:
    valor_logico = False
    


print(fatorial(num, valor_logico))
print(fatorial(num))

help(fatorial)
