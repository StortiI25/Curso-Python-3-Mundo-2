 #Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para tabuada: '))
print (f'A tabuada do {n} é: \n') 

for t in range(1,11):
    print(f'{n} x {t:2} = {n*t}')