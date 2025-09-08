#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de PA')
print('-=-'*10)
primeira = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeira
cont = 1
while cont <= 10:
    print(f'{termo} ->',end=" ")
    termo += razao
    cont += 1
print('FIM')

