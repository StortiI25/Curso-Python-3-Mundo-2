#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 40)
print("{:^40}".format("BANCO PYTHON"))
print("=" * 40)

valor = int(input("Qual valor você deseja sacar? R$ "))

cedulas = [50, 20, 10, 1]  
for ced in cedulas:
    qtd = valor // ced      
    valor = valor % ced    
    if qtd > 0:
        print(f"Total de {qtd} cédula(s) de R${ced}")

print("=" * 40)
print("Volte sempre ao BANCO PYTHON! Tenha um bom dia!")
print("=" * 40)
