#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
tot18 = toth = totm = 0
while True:
    i = int(input('Digite a idade: '))
    s = " "
    while s not in 'MF' :
        s = str(input('Digite o Sexo: [M/F] ')).strip().upper()[0]
    if i >= 18:
        tot18 += 1
    if s == 'M':
        toth += 1
    if s == 'F' and i < 20:
        totm += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos são {tot18}')
print(f'Ao todo temos {toth} homens cadastrados ')
print(f'E temos {totm} mulheres com menos de 20 anos')
print('Acabou!')
