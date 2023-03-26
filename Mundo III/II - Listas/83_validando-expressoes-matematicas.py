# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = input('Digite a expressão: ').strip()

lista_parenteses = []

for elemento in exp:
    if elemento == '(':
        lista_parenteses.append(elemento)
    elif elemento == ')':
        if len(lista_parenteses) > 0:
            lista_parenteses.pop()
        else:
            lista_parenteses.append(')')
            
if len(lista_parenteses) == 0:
    print('Expressão validada.')
else:
    print('Expressão não validada.')