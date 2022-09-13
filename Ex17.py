#Exercício 17 - Entrar com o peso, o sexo e a altura de uma determinada pessoa. 
# Após a digitação, exibir se esta pessoa está ou não com seu peso ideal. 
# Fórmula: peso/altura².

peso = float(input('Informe o seu peso(kg): '))
altura = float(input('Informe a sua altura(m): '))
sexo = input('Informe o seu gênero(F/M): ')

imc = peso / (altura * altura);

if(sexo.upper() == "F"):
	if(imc < 19):
		print("Abaixo de peso")
	elif(imc < 24):
		print("Peso ideal")
	else:
		print("Acima do peso")
else:
	if(imc < 20):
		print("Abaixo de peso")
	elif(imc < 25):
		print("Peso ideal")
	else:
		print("Acima do peso")
