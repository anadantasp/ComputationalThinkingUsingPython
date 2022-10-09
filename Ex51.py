#Exercício 51 - Armazenar dez números na memória do computador. Exibir os valores na ordem 
#inversa à da digitação

numeros = []

for i in range(0, 10, 1):
    num = int(input('Digite um número: '))
    numeros.append(num)

print('Números digitados em ordem decrescente: ')

for i in range(9, -1, -1):
    print(numeros[i])
