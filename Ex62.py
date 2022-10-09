#Exercício 62 - Armazenar o nome, sexo e idade de vinte pessoas. 
#Após a digitação, exibir os dados (nome, sexo e idade) em ordem 
#decrescente de idade

nomes = []
sexos = []
idades = []

for i in range(0,3,1):
    nome = input('Digite o nome: ')
    nomes.append(nome)
    sexo = input('Gênero: ')
    sexos.append(sexo)
    idade = int(input('Digite a idade: '))
    idades.append(idade)

for i in range(0,3,1):
    for j in range(i+1, 3, 1):
        if(idades[i]<idades[j]):
            auxIdade = idades[i]
            idades[i] = idades[j]
            idades[j] = auxIdade

            auxNome = nomes[i]
            nomes[i] = nomes[j]
            nomes[j] = auxNome

            auxSexo = sexos[i]
            sexos[i] = sexos[j]
            sexos[j] = auxSexo


for i in range(0,3,1):
    print(nomes[i])
    print(sexos[i])
    print(idades[i])







