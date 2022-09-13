#Exercício 31 - Criar uma rotina de entrada que aceite somente um valor positivo

num = int(input('Digite um número: '))

while(num < 0):
    print('Opa! Não pode número negativos.')
    num = int(input('Digite outro número: '))

print('Número digitado válido')
