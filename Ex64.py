#Exercício 64 - Armazenar no máximo vinte valores em um vetor. Exibir a 
#quantidade de valores pares e ímpares. Exibir também o percentual da 
#quantidade de valores pares e ímpares

numeros = []

for i in range(0,10,1):
    numeros.append(int(input('Digite um número: ')))

quantPar = 0 
quantImpar = 0

for i in range(0,10,1):
    if(numeros[i] % 2 == 0):
        quantPar = quantPar + 1
    else:
        quantImpar = quantImpar + 1

parPerc = (quantPar * 100) / 10
imparPerc = (quantImpar * 100)/10

print("Quantidade de números PARES: ", quantPar)
print("Quantidade de números ÍMPARES: ", quantImpar)
print(f"Porcentagem de números PARES: {parPerc}%")
print(f"Porcentagem de números ÍMPARES: {imparPerc}%")
