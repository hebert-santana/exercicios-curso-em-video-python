# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                                
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)

def notas(notas):
    dicionario = {}
    dicionario['Quantidade Notas'] = len(notas)    
    dicionario['Maior Nota'] = max(notas)
    dicionario['Menor Nota'] = min(notas)
    dicionario['Média'] = round(sum(notas)/len(notas), 2)
    return dicionario

lista_notas = []
while True:
    nota = float(input('Digite uma nota: '))
    lista_notas.append(nota)
    continuar = str(input('[S] - sim\n[N] - não\nDeseja inserir mais uma nota? ')).strip().upper()[0]
    if continuar == 'N':
        break
    
    
print(notas(lista_notas))
    