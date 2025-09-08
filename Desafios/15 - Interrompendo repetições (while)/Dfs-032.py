#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um valor para tabuada: '))
    if n < 0:
        break
    print('-=-'*15)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-=-'*15)
print('Programa da tabuada encerrado! Volte sempre.')