#Exercício 53 - Armazenar vinte valores em um vetor. Após a digitação, entrar com uma constante 
#multiplicativa que deverá multiplicar cada um dos valores do vetor e armazenar o resultado no 
#próprio vetor, na respectiva posição

numeros = []

for i in range(0, 20, 1):
    num = int(input('Digite um número: '))
    numeros.append(num)

const = int(input('Entre com a constante multiplicativa: '))

#for i in range(0, 20, 1):
#    print(f'{numeros[i]} X {const} = {numeros[i] * const}')

for i in range(0, 20, 1):
    numeros[i] = numeros[i] * const
    print(numeros[i])
