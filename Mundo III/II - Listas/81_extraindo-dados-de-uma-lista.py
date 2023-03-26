# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
contador = 0

while True:
    n = float(input('Digite um número: '))
    lista.append(n)
    
    if n == 5:
        contador += 1
        
    continuar = input('[S] - sim\n[N] - não\nDeseja continuar? ').upper().strip()[0]
    if continuar == 'N':
        print('Saindo do gerador de lista...')
        break
    elif continuar == 'S':
        continue
    else:
        print('Resposta inválida. Vai continuar por default.')
    
print(f'Lista original: {lista}')       
print(f'Foram digitador {len(lista)} números.')

lista.sort(reverse=True)
print(f'A lista ordenada em ordemn descrescente é: {lista}')

if 5 in lista:
    print(f'O número 5 apareceu {contador} vezes na lista.')
else:
    print('O número 5 não aparece na lista.')