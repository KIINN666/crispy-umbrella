somaidade = 0 
media_idade = 0 
maior_idade_men = 0 
nome_mais_velho = 0 
for c in range (1,5):
    print(f'-------{c}º PESSOA  ---------',)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade '))
    sexo = str(input('Sexo ')).strip()
    somaidade += idade 
    if c == 1 and sexo in 'Mm':
        maior_idade_men = idade
        nome_mais_velho = nome 
    if sexo in 'Mm' and idade > maior_idade_men: 
        maior_idade_men = idade
        nome_mais_velho = nome 
media_idade = somaidade / 4
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_men} anos e se chama {nome_mais_velho}')
