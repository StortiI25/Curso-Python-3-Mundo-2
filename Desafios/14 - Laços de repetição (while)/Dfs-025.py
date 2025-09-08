#Faça um programa que leia um número qualquer e mostre o seu Fatorial.

#Ex:
#5! = 5x4x3x2x1 = 120
n1 = int(input('Digite seu numero para calcular o fatorial: '))
c = n1
f = 1
print(f'Calculando {n1}! = ',end="")
while c > 0:
    print(f'{c}',end="")
    print(' x ' if c > 1 else ' = ',end="")
    f *= c
    c -= 1
print(f'{f}')