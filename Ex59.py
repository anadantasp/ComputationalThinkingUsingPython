#Exercício 59 - Alterar o programa anterior, no sentido de controlar o 
#layout final de tela, para que o usuário pressione uma tecla para 
#visualizar os dados das pessoas passo a passo, por exemplo, de dez em dez
#pessoas


nomes = []
idades = []
sexos = []

for i in range(0,5,1):
    nome = input('Digite o nome: ')
    nomes.append(nome)
    idade = int(input('Digite a idade: '))
    while(idade <= 0):
        print('Digite uma idade válida!')
        idade = int(input('Digite a idade: '))
    idades.append(idade)
    sexo = input('Digite o sexo: ').upper()
    while( sexo != 'F' and sexo != 'M'):
        print('Ops! Entrar com valores F ou M apenas')
        sexo = input('Digite o sexo: ').upper()
    sexos.append(sexo)

quant = 0
tecla = 0

for i in range(0,5,1):
    if(idades[i] > 18):
        if(tecla == 2):
            input("Precione uma tecla pra continuar")
    
            tecla = 0
            print('Nome: ', nomes[i])
            print('Idade: ', idades[i])
            print('Sexo: ', sexos[i])

            quant = quant + 1
            tecla = tecla + 1
        else:
            print('Nome: ', nomes[i])
            print('Idade: ', idades[i])
            print('Sexo: ', sexos[i])

            quant = quant + 1
            tecla = tecla + 1

print('Quantidade de pessoas maiores de 18: ', quant)