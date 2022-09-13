#Exercício 26 - Encontrar o dobro de um número caso ele seja positivo e o seu triplo 
#caso seja negativo, imprimindo o resultado.

num = int(input('Digite um número: '))

if(num > 0):
    dobro = num * 2
    print(f'DOBRO: {num}')
else:
    triplo = num * 3
    print(f'TRIPLO: {num}')