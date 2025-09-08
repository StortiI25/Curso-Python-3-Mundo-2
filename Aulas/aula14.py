n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um Numero: '))
    if n != 0: 
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Voce digitou {par} numero(s) pare(s) e {impar} numero(s) impar(s)')

    
