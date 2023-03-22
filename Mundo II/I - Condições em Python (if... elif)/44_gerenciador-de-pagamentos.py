# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço do produto: "))

while True:
    pagamento = int(input("\n----- Formas de Pagamento -----\n[1] - à vista dinheiro/cheque\n[2] - à vista no cartão\n[3] - em até 2x no cartão\n[4] - 3x ou mais no cartão\n\nDigite a forma de pagamento: "))
    if pagamento in [1, 2, 3, 4]:
        break
    else:
        print('Forma de pagamento inválida.')
        
if pagamento == 1:
    preco_final = preco * 0.9
elif pagamento == 2:
    preco_final = preco * 0.95
elif pagamento == 3:
    preco_final = preco
    parcelas = preco_final / 2
    print(f"O produto será parcelado em 2x de R${parcelas:.2f} sem juros.")
elif pagamento == 4:
    preco_final = preco * 1.2
    num_parcelas = int(input("Digite o número de parcelas: "))
    parcelas = preco_final / num_parcelas
    print(f"O produto será parcelado em {num_parcelas}x de R${parcelas:.2f}.")


print(f"O preço final do produto é R${preco_final:.2f}.")