# Exercício Python 112: Dentro do pacote uteis que criamos teremos um módulo chamado dado. 
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from uteis import moedas

v = moedas.leiaDinheiro('Digite um valor: R$ ')
moedas.resumo(v)