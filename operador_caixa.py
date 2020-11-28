# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto            - em até 2x no cartão: preço normal 
# - à vista no cartão: 5% de desconto                   - 3x ou mais no cartão: 20% de juros 

price_product = float(input('insira o preço do produto:')) 
form_payment = input('Qual a forma de pagamento:')

in_cash = (price_product*0.10 - price_product)*(-1)
on_card = price_product*0.05 - price_product
card_installmente_2x = price_product
card_installmente_more = price_product*0.2 + price_product

if form_payment == 'à vista':
    print(f'O produto sairá por R$: {in_cash}')
elif form_payment == 'à vista no cartão':
    print(f'O produtor sairá por R$: {on_card}')
elif form_payment == '2x no cartão':
    print(f'O produto sairá por R$: {card_installmente_2x}')
else:
    print(f'O produto sairá por R$: {card_installmente_more}')

