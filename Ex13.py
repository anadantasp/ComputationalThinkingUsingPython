#Exercício 13 - Entrar via teclado com três valores distintos. Exibir o maior deles.


num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if(num1 > num2 and num1 > num3):
    print(f"{num1} é o maior valor digitado")
elif(num2 > num1 and num2 > num3):
    print(f"{num2} é o maior valor digitado")
else:
    print(f"{num3} é o maior valor digitado")
