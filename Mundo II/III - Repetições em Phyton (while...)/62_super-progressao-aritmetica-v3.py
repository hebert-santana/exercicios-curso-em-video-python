# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

qnt_termos = 10

termo = int(input('Digite o termo inicial da PA: '))
r = int(input('Digite a razão da PA: '))

print('Progressão Aritmética: ', end='')
while qnt_termos != 0:
    print(termo, end= ' ')
    termo += r
    qnt_termos -= 1
    if qnt_termos == 0:
        mais_termos = str(input('\n\n[S] - sim\n[N] - não\nDejesa mostrar mais termos? ')).upper().strip()[0]
        if mais_termos == 'S':
            qnt_termos = int(input('Digite mais quantos ternmos dejesa mostrar: '))
        elif mais_termos == 'N':
            break
        else:
            print('Resposta Inválida.')