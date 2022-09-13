#Exercício 25 - Faça um algoritmo para receber um número qualquer e informar na tela 
# se é par ou ímpar. Utilize o operador %

num = int(input('Digite um número: '))

if(num % 2 == 0):
    print('Esse número é PAR')
else:
    print('Esse número é "ÍMPAR"')