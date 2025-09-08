#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#Média abaixo da 5.0: REPROVADO
#Média entre 5.0 a 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

np1 = int(input('Digite a NP1: '))
np2 = int(input('Digite a NP2: '))
pim = int(input('Digite o PIM: '))

soma = (np1  + np2  + pim)  / 3

if soma >= 7 :
    print(f'Parabéns foi APROVADO! A Sua media foi {soma:.1f} ')
elif soma >= 5:
    print(f'Estude mais você está de RECUPERAÇÃO! Sua media foi {soma:.1f}')
else :
    print(f'Não foi dessa vez REPROVADO! Sua media foi {soma:.1f}')