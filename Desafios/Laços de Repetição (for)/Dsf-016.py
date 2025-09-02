#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
menores = 0
maiores = 0

for i in range(1,8):
    ano = int(input(f'Digite o seu ano de nacimento da {i}ª Pessoa: '))
    idade = ano_atual - ano

    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'\nAo todo tivemos {maiores} pessoas maiores de idade.')
print(f'E tambem tivemos {menores} pessoas menores de idade.')