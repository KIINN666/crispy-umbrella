in_number_one = int(input('insira um número: '))
in_number_two = int(input('insira um segundo número: '))
c = 0
while c == 0: 
    
    in_menu = int(input('escolha uma ação: \n [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA \n---> '))
    if in_menu == 1:
        print(f'A soma de {in_number_one} + {in_number_two} é igual à: {in_number_one + in_number_two}')
        
    elif in_menu == 2:
        print(f'A multiplicação de {in_number_one} por {in_number_two} é igual à: {in_number_one*in_number_two}')
    elif in_menu == 3: 
        if in_number_one > in_number_two:
            print(f'o número {in_number_one} é maior')
        elif in_number_one < in_number_two:
            print(f'o número {in_number_two} é maior') 
        elif in_number_one == in_number_two:
            print('Os dois números são iguais')
    elif in_menu == 4:
        in_number_one = int(input('insira um número: '))
        in_number_two = int(input('insira um segundo número: '))
    elif in_menu == 5:
        print('GOOD BYE!')
        c += 1
