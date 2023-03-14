# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Salário do Funcionário: R$ '))
reajuste = 0.15

s_reajustado = s + s * reajuste

print(f'A salário antigo era: R$ {s}')
print(f'Salário após o reajuste: R$ {s_reajustado}')