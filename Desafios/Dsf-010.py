#Cria um programa que faça o computador jogar Jokenpô com você.
import random
opcao = ['pedra','tesoura','papel']

jogador = input('Escolha (pedra, papel ou tesoura): ').lower()
cpu = random.choice(opcao)

print ('Você jogou:', jogador)
print ('CPU jogou:', cpu)

if jogador == cpu :
    print('Empate!')
elif(jogador == "pedra" and cpu == "tesoura" ) or \
    (jogador == "tesoura" and cpu == "papel") or \
    (jogador == "papel" and cpu == "pedra"):
    print('Você GANHOU!')
else:
    print ('Você PERDEU!')
    

