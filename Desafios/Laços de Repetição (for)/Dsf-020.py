#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Termo: '))
razao = int(input('Razão: '))
dec = n1 + (10 - 1) * razao

for c in range(n1, dec + razao, razao):
    print(f'{c}',end=" → ")
print('ACABOU')