#Exercício 23 - Faça um algoritmo que leia os valores A, B, C e imprima na tela se a 
# soma de A + B é menor que C.

a = int(input('Entre com o primeiro número: '))
b = int(input('Entre com o segundo número: '))
c = int(input('Entre com o terceiro número: '))

soma = a + b

if(soma < c):
    print(f'{a} + {b} < {c}')
    print(f'{soma} < {c}')
else:
    print('A soma de A + B é MAIOR que C')

