# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Digite um numero: '))

print('''Escolhe a base de converção
[1] Binráia
[2] octal
[3] hexadecimal''')

opcao = int(input('Qual é sua opção? '))

if opcao == 1:
    print(f'{num} convertido para BINARIO {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL {hex(num)[2:].upper()}')
else :
    print('Opção invalida! Tente novamente.')

