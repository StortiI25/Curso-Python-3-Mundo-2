#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 a 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima da 40: Obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

if imc >= 40 :
    print(f'IMC de {imc}: Obesidade mórbida')
elif imc >= 30:
    print(f'IMC de {imc}: Obesidade')
elif imc >= 25:
    print(f'IMC de {imc}: Sobrepeso')
elif imc >= 18.5 :
    print(f'IMC de {imc}: Peso ideal')
else :
    print(f'IMC de {imc}: Abaixo do Peso')
