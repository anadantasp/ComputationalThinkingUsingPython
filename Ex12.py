#Exercício 12 - Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão digitados. 
#Se a área for maior que 100, exibir a mensagem “Terreno grande”, caso contrário, exibir a mensagem “Terreno pequeno”.

print('------ Calculando a área de um retângulo ------')
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area = base * altura

if(area > 100):
    print("Área: ", area)
    print("Terreno grande")
else:
    print("Área: ", area)
    print("Terreno pequeno")