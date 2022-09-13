#Exercício 16 - Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. 
# Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos

a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = int(input("Digite o valor C: "))

if (((a + b) > c) and ((b + c) > a) and (a + c > b)):
    print("Estes valores formam um triangulo")
    if(a > b and a > c ):
        if((a * a) == (b * b) + (c * c)):
            print("E este triângulo é retângulo")
    elif(b > a and b > c):
        if((b * b) == (a * a) + (c * c)):
            print("E este triangulo é retângulo")
    elif(c > a and c > b):
        if((c * c) == (a * a) + (b * b)):
            print("E este triangulo é retângulo")
    else:
        print("E este triângulo não é retângulo")
else:
    print("Esses valores não formam um triangulo!")