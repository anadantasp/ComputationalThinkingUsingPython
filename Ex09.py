#Exercício 9 - Entrar via teclado, com dois valores distintos. Exibir o menor deles.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if(num1 < num2):
    print('Menor valor digitado: ', num1)
else:
    print('Menor valor digitado: ', num2)