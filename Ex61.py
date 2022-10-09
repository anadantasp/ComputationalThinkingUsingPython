#Exercício 61 - Armazenar vinte valores em um vetor. Após a digitação, 
#exibir os valores em ordem decrescente

numeros = []

for i in range(0,5,1):
    numeros.append(int(input('Digite um número: ')))

for i in range(0,5,1):
    for j in range(i+1,5,1):
        if(numeros[i] < numeros[j]):
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

for i in range(0,5,1):
    print(numeros[i])