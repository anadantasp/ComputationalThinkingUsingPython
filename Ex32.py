#Exercício 32 - Entrar com dois valores via teclado, onde o segundo deverá ser maior 
#que o primeiro. Caso contrário solicitar novamente apenas o segundo valor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while(num2 < num1):
    print('O segundo valor deve ser maior que o primeiro')
    num2 = int(input('Digite o segundo número novamente: '))

print('Dados digitados válidos')
