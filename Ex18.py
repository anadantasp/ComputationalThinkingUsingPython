#Exercício 18 -  Criar um programa para analisar a velocidade de um automóvel. 
# Solicitar via teclado os valores da aceleração (a em m/s2), velocidade inicial (v0 em m/s) e o tempo de percurso (t em s). 
# Calcular e exibir a velocidade final do automóvel em km/h. E exibir mensagem de acordo com a tabela abaixo:

a = float(input('Entre com o valor da aceleração (m/s²): '))
v0 = float(input('Entre com o valor da velocidade inicial (m/s): '))
t = float(input('Entre com o tempo do percuso (em segundos): '))

v = v0 + a * t
		
v = v * 3.6

print('Velocidade do veículo: {:.2f}'.format(v))

if(v <= 40):
    print('Veículo muito lento')
elif(v <= 60):
    print('Velocidade permitida')
elif(v <= 80):
    print('Velocidade de cruzeiro')
elif(v <= 120):
    print('Veículo rápido')
else:
    print('Veículo muito rápido')
