#Exercício 11 - Calcular e exibir a área de um retângulo, 
# a partir dos valores da base e altura que serão digitados. 
# Se a área for maior que 100, exibir a mensagem “Terreno grande”.

print('------ Calculando a área de um retângulo ------')
base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))

area = base * altura

if(area > 100):
    print("Terreno grande")
