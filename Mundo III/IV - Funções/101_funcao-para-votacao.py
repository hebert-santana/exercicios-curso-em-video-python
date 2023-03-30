# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade >= 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


ano_nascimento = int(input('Digite o ano de nascimento: '))
print(f'Situação do voto: {voto(ano_nascimento)}')
