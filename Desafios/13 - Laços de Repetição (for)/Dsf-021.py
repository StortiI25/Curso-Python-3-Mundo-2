# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#▸ A média da idade do grupo.
#▸ Qual é o nome do homem mais velho.
#▸ Quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0

for p in range(1, 5):
    print(f'------------{p}º PESSOA ------------')
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1


mediaidade = somaidade / 4 
print (f'A media de idade do grupo é de {mediaidade} anos')
print (f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print (f'O total de mulher com menos de 20 anos é {totmulher}')