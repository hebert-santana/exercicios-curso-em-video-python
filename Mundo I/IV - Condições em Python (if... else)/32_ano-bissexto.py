# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Regra de ano bissexto: deve ser divisível por 4 / se divisível por 100, deve ser divisível por 400

while True:
    ano = int(input('Digite o ano: '))
    
    if ano > 0:
        
        if ano % 4 == 0:
            
            if ano % 100 == 0:
                
                if ano % 400 == 0:
                    print(f'O ano {ano} é bissexto.')
                    break
                else:
                    print(f'O ano {ano} não é bissexto.')
                    break
                
            print(f'O ano {ano} é bissexto.')
            break
        else:
            print(f'O ano {ano} não é bissexto.')
            break
    else:
        print('Ano Inválido.')
        
# exemplo: 2000 foi um ano bissexto porque é divisível por 400, mesmo sendo um múltiplo de 100. Já o ano 1900 não foi um ano bissexto porque é um múltiplo de 100, mas não é divisível por 400.