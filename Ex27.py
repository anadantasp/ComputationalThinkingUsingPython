#Exercício 27 - Faça um algoritmo que leia uma variável e some 5 caso seja par ou 
#some 8 caso seja ímpar, imprimir o resultado desta operação

num = int(input('Digite um número: '))

if(num % 2 == 0):
    soma = num + 5
    print(f'Soma: {soma}')
else:
    soma = num + 8
    print(f'Soma: {soma}')