 #Escreva um programa para aprovar o empréstimo bancário para a compra da uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ela vai pagar.

#Calcula o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Quanto é o seu salario? '))
anos = int(input('Quantos anos para pagar? '))

parcelas = casa / (anos * 12)
salario_30 = salario * 0.30

if parcelas > salario_30 :
    print(f'as parcelas de {parcelas:.2f} excede 30% do seu salario, EMPRESTIMO NEGADO! ')
elif parcelas < salario_30:
    print(f'As parcelas ficaram {parcelas:.2f} e 30% do seu salario é {salario_30}, EMPRETISMO APROVADO! Aproveite sua casa.')
    




