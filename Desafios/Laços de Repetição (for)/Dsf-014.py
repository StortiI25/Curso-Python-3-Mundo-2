#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
divisores = 0

for i in range (1,num + 1):
    if num % i == 0:
        print(f'\033[33m', end=" ")
        divisores += 1
    else:
        print('\033[31m', end=" ")
    print(f'{i}', end=" ")
print(f'\n\033[mO número {num} foi divisível {divisores} vezes')

if divisores == 2:
    print(f'É um número primo ✅')
else:
    print(f'Não é um número primo ❌')