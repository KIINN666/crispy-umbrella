#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário 
# do comprador e em quantos anos ele deseja pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 

house_price = int(input('insira o valor da casa:'))
salary_buyer = int(input('qual sua renda mensal:'))
years_pay = int(input('em quantos anos deseja pagar? '))
installmente_number = years_pay*12
installment_valor = house_price/(years_pay*12)


if salary_buyer*0.30 < house_price/(years_pay*12):
    print('IMPRÉSTIMO NEGADO!')
     
else:
    print('IMPRÉSTIMO APROVADO!')
    print(f'O valor da prestação será de {installmente_number}X de R$:{installment_valor:.3f} ') #   :.(quantiadde de casas decimais depois da vígula que deseja por)f
                                                                                                 #   só foi testado usando a função f-string  
