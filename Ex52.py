#Exercício 52 - Armazenar dez valores na memória do computador. Após a digitação dos valores, 
#criar uma rotina para ler os valores e achar e exibir o maior deles.

numeros = []

for i in range(0, 10, 1):
    num = int(input('Digite um número: '))
    numeros.append(num)

for i in range(0,10, 1):
    if(i == 0):
        maior = numeros[0]
    elif(numeros[i] > maior):
        maior = numeros[i]

print(f'O maior número digitado foi {maior}')