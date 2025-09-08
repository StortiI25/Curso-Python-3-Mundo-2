#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] soamar
    [2] mutiplicar
    [3] maior
    [4] novos numeros]
    [5] sair do programa''')
    opcao = int(input('Qual sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'a soma de {n1} + {n2} é {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'Multiplicação de {n1} x {n2} é {mult}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        print('Informe os numeros novamente.')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente.')
    print('-=-'*10)
    sleep(1)
print('Fim do programa. Volte sempre.')