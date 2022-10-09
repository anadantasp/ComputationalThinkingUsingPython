#Exercício 57 - Armazenar o nome, sexo e idade de cem pessoas. Consistir 
#as entradas no sentido de aceitar apenas “F” ou “M” para o sexo e valores 
#positivos para a idade. Após a digitação dos dados, exibir os dados 
#(nome, sexo e idade) de todas as pessoas do sexo feminino.


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

for i in range(0,5,1):
    if(sexos[i] == 'F'):
        print('Nome: ', nomes[i])
        print('Idade: ', idades[i])
        print('Sexo: ', sexos[i])

