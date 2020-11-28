# 03.Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres)

in_name = str(input('insira seu nome: '))
in_age = int(input('digite sua idade: '))
in_salary = float(input('digite seu salário: '))
in_genere = str(input('digite seu sexo: ')).upper()
in_marital_status = str(input('Estado Civil: '))

while len(in_name) < 3:
    in_name = str(input('*o nome precisa conter no mínimo 3 letras: '))
while 0 < in_age > 150:
    in_age = int(input('*você precisa ter entre 0 e 150 anos... '))
while in_salary <= 0: 
    in_salary =  float(input('*seu salário precisa ser maior que zero...'))
while in_genere not in 'FM':
    in_genere = str(input('*Digite "M" para masculino e "F" para mulher:...'))
while in_marital_status not in 'SCVD':
    in_marital_status = str(input('*digite "s" para solteiro \n "c" para casado \n "v" para viúvo \n ou "D" para divorciado...'))

print(f'Nome:{in_name} \n Idade:{in_age} \n Renda:{in_salary} \n Sexo:{in_genere} \n Estado Civil:{in_marital_status}' )
