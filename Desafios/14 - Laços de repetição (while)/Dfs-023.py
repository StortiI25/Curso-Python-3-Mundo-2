#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('-=-'*20)
print('Pensei em um numero de 0 a 10, Tente adivinhar!!')
print('-=-'*20)

cpu = randint(0,10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Digite um numero: '))
    palpites += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('MAIS... Tente novamente!')
        else:
            print('MENOS... Tente novamente!') 

print(f'Você Acertou, com {palpites} tentativas')
