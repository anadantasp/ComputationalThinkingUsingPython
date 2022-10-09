#Exercício 54 - Armazenar vinte valores na memória. Após a digitação, entrar com uma constante 
#multiplicativa que deverá multiplicar cada um dos valores do vetor e armazenar o resultado em 
#outro vetor, porém em posições equivalentes. Exibir os vetores na tela.

numeros = []
res = []

for i in range(0, 20, 1):
    num = int(input('Digite um número: '))
    numeros.append(num)

const = int(input('Entre com a constante multiplicativa: '))

for i in range(0, 20, 1):
    res.append(numeros[i] * const)
    print(f'{numeros[i]} X {const} = {res[i]}')