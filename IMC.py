# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status de acordo com a tabela abaixo:
# abaixo de 18.5: Abaixo do Peso                     25 à 30: Sobrepeso             acima de 40: Obesidade Mórbida  
# Entre 18.5 e 25: Peso Ideal                       30 à 40: Obesidade 

weight = float(input('insira seu peso (kg):'))
height = float(input('insira sua altura (m)'))

IMC = weight/(height)**2
print(f'seu IMC é: {IMC:.2f}')
if IMC < 18.5:
    print('Abaixo do Peso!')
elif 18.5 <= IMC <= 25:
    print('Peso Ideal')
elif 25 < IMC <= 30: 
    print('Sobrepeso')
elif 30 > IMC >= 25:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade Morbida!')
