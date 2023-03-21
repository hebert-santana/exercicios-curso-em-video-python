# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

v = float(input('Digite o valor da casa: R$ '))
s = float(input('Digite seu salário: R$ '))
t = float(input('Digite tempo (em anos) do empréstimo: '))

# considerando que não há juros
t_meses = t * 12
prestacao_mensal = v / t_meses

if prestacao_mensal > (s * 0.3):
    print('Empréstimo negado.')
else: 
    print('Empréstimo aprovado.')
    print(f'Você vai pagar {t_meses} parcelas mensais de R$ {round(prestacao_mensal)}')
    