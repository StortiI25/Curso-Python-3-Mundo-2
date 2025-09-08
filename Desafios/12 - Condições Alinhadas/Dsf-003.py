# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

num1 = int(input('Digite PRIMEIRO numero: '))
num2 = int(input('Digite SEGUNDO numero: '))

if num1 > num2:
    print(f'Primeiro numero é MAIOR')
elif num2 > num1 :
    print(f'Segundo numero é MAIOR')
else :
    print(f'numeros são IGUAIS')

