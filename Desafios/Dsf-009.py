# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

valor = int(input('Qual valor do produto? '))

print('-------------------------------------')

print('Qual a forma de pagamento? ')
print('[1] Dinheiro/Cheque')
print('[2] Cartão á vista')
print('[3] Até 2x sem juros')
print('[4] 3x com juros de 20% \n -----------------------------------' )

opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1 :
    print(f'Á vista no dinheiro ficará: {valor - (0.10 * valor):.2f}R$ ')
elif opcao == 2 :
    print(f'Á vista no cartão ficará: {valor - (valor * 0.05):.2f}R$')
elif opcao == 3 :
    print(f'Em 2x no cartão ficará: {valor:.2f}R$')
elif opcao == 4 :
    print(f'em 3x com juros de 20% ficará:  {valor + (valor * 0.20):.2f}R$')
else :
    print('Opção Invalida! Tente novamente.')