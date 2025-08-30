#Faça um programa que leia o ano de nascimento de um jovem e o informe, de acordo com sua idade:

#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

data = int(input('Qual ano de nacimento? '))
ano_atual = date.today().year
idade = ano_atual - data

print (f'Quem naceu em {data} tem {idade} anos em {ano_atual}')

if idade < 18:
    saldo = 18 - idade
    ano_alist= ano_atual + saldo
    print(f'Ainda falta {saldo} ano(s) para o alistamento.')
    print(f'Seu alistamento sera em {ano_alist}')
elif idade == 18:
    print('Deve se alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    ano_alist = ano_atual - saldo
    print(f'Você devereia ter se alistado há {saldo} ano(s).')
    print(f'Seu alistamento foi em {ano_alist}.')


