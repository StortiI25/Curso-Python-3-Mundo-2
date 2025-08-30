
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Refaça o DESAFIO dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

a = float(input('Digite o lado a do triangulo: '))
b = float(input('Digite o lado b do triangulo: '))
c = float(input('Digite o lado c do triangulo: '))

if a < b + c and b < a + c and c < a + b:

    if a == b == c :
        print('Triângulo do tipo: EQUILÁTERO')
    elif a == b or a == c or b == c :
        print('Triângulo do tipo: ISÓSCELES')
    else :
        print('Triângulo do tipo: ESCALENO')
else :
    print('As retas NÃO pode formar um triângulo!')