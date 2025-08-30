# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print(f'Primeiro numero {num1} é maior que o Segundo numero {num2}')
elif num2 > num1 :
    print(f'Segundo numero {num2} maior que primeiro numero {num1}')
else :
    print(f'Primero numero {num1} igual segundo numero {num2}')

