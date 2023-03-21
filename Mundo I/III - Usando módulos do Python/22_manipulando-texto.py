# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome:  ')).upper().strip()
print(f'Seu nome em maiúsculo: {nome}.')
print(f'Seu nome em minúsculo: {nome.lower()}.')


nome_sem_espaco = nome.replace(' ', '')
print(f'Quantidade de letras no nome: {len(nome_sem_espaco)}.')

primeiro_nome = nome.split()[0]
print(f'Quantidade de letras no primeiro nome: {len(primeiro_nome)}.')