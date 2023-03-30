# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

funcionario = {}

funcionario['Nome'] = str(input('Digite o nome do funcionário: ')).strip().title()
data_nascimento = input('Digite a data de nascimento (XX/XX/XXXX): ').strip()
funcionario['CTPS'] = int(input('Digite o número da carteira de trabalho: '))


ano_nascimento = int(data_nascimento[-4:])
ano_atual = datetime.now().year

funcionario['Idade'] = ano_atual - ano_nascimento

if funcionario['CTPS'] != 0:
    funcionario['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    funcionario['Salário'] = float(input('Digite o salário: R$ '))
    
    # considerando que a pessoa deve ter 35 anos de contribuição para se aposentar
    dt_contratacao = funcionario['Ano de Contratação']
    tempo_contribuicao = ano_atual - dt_contratacao
    t_aposentar = 35 - tempo_contribuicao

    funcionario['Idade Aposentar'] = funcionario['Idade'] + t_aposentar

print('\n===================== FUNCIONARIO =====================')
for k, v in funcionario.items():
    print(f'{k} = {v}')
    




