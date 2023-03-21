# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite seu salário: R$ '))

if s >= 0 and s <= 1250:
    s_reajustado = s * 1.5
elif s > 1250:
    s_reajustado = s * 1.1
else:
    print('Salário Inválido.')

aumento = s_reajustado - s
    
print(f'Salário antigo: R${s}')
print(f'Salário reajustado: R${s_reajustado}')
print(f'Total do aumento: R${aumento}')