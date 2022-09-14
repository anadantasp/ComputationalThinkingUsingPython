#Entrar via teclado com “N” valores quaisquer. O valor “N” (que representa a quantidade de números) será digitado, deverá ser
#positivo, mas menor que vinte. Caso a quantidade não satisfaça a restrição, enviar mensagem de erro e solicitar o valor 
#novamente. Após a digitação dos “N” valores, exibir:
#a) O maior valor;
#b) O menor valor;
#c) A soma dos valores;
#d) A média aritmética dos valores;
#e) A porcentagem de valores que são positivos;
#f) A porcentagem de valores negativos;

soma = 0
positivos = 0
negativos = 0

quant = int(input('Quantidade de números que serão digitados: '))

while(quant < 0 or quant >=20):
    print('Opa! Não pode números negativos e quantidade deve ser menor que 20')
    quant = int(input('Quantidade de números que serão digitados: '))


for quant in range(1, quant + 1, 1):
    num = int(input('Digite um número: '))

    #while(num < 0):
    #    print('Opa! Não pode números negativos!')
    #    num = int(input('Digite outro número: '))
    
    if(quant == 1):
        maior = num
    else:
        if(num > maior):
            maior = num

    if(quant == 1):
        menor = num
    else:
        if(num < menor):
            menor = num

    if(num > 0):
        positivos = positivos + 1
    else:
        negativos = negativos + 1

    soma = soma + num

media = soma / quant

porcentagemPositivo = (positivos * 100) / quant
porcentagemNegativo = (negativos * 100) / quant

print('O maior valor: ', maior)
print('O menor valor: ', menor)
print('Soma dos valores: ', soma)
print('Média: ', media)
print('Porcentagem dos valores positivos: ', porcentagemPositivo)
print('Porcentagem dos valores : ', porcentagemNegativo)
