#Exercício 36 - Entrar via teclado com um valor (X) qualquer. Travar a digitação, 
# no sentido de aceitar somente valores positivos. Solicitar o intervalo que o 
# programa que deverá calcular a tabuada do valor digitado, sendo que o segundo valor 
#(B), deverá ser maior que o primeiro (A), caso contrário, digitar novamente somente o 
#segundo. Após a validação dos dados, exibir a tabuada do valor digitado, no intervalo 
#decrescente, ou seja, a tabuada de X no intervalo de B para A.



num = int(input("Digite um número: "))

while(num <= 0):
    print("Opa! Não pode números negativos, apenas positivos!")
    num = int(input("Digite um número: "))

a = int(input("Digite o início do intervalo: "))
b = int(input("Digite o fim do intervalo: "))

while (b <= a):
    print("Opa! É necessário que o valor de b seja maior que o de a")
    b = int(input("Digite o fim do intervalo: "))

for b in range(b, a - 1, -1):
    res = num * b
    print(f'{num} X {b} = {res}')
