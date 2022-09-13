#Exercício 15 - A partir de três valores que serão digitados, verificar se formam ou não um triângulo. Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”. 
# Um triângulo escaleno possui todos os lados diferentes, o isósceles, dois lados iguais e o eqüilátero, todos os lados iguais. 
# Para existir triângulo é necessário que a soma de dois lados quaisquer seja maior que o outro, isto, para os três lados.

a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = int(input("Digite o valor C: "))

if (((a + b) > c) and ((b + c) > a) and ((a + c) > b)):
    print("Estes valores formam um triangulo")
    if(a != b and c != b and c != a):
        print("E este triângulo é ESCALENO")
    elif(a == b and a != c or c == b and c != a or c == a and c != b):
        print("E este triângulo é ISÓSCELES")
    else:
        print("E este triângulo é EQUILÁTERO")
else:
    print("Esses valores não formam um triangulo!")