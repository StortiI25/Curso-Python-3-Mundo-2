#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

from datetime import date

data = int(input('Digite o ano de nacimento: '))
ano_atual = date.today().year
idade = ano_atual - data

if idade <= 9:
    print(f'Você tem {idade} ano(s), atleta MIRIM')
elif idade < 14 :
    print(f'Você tem {idade} ano(s), Atleta INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} ano(s), Atleta JUNIOR')
elif idade == 20 :
    print(f'Você tem {idade} ano(s), Atleta SÊNIOR')
else :
    print(f'Você tem {idade} ano(s), Atleta MASTER')
