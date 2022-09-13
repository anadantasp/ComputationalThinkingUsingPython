#Exercício 10 - Entrar com dois valores quaisquer. Exibir o maior deles, se existir, 
# caso contrário, enviar mensagem avisando que os números são idênticos.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if(num1 > num2):
    print(f"Maior valor digitado: {num1}")
elif(num2 > num1):
    print(f"Maior valor digitado: {num2}")
else:
    print("Os dois valores são iguais")