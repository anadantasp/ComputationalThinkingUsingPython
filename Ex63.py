#Exercício 63 - Armazenar o nome, sexo e idade de vinte pessoas. Após a 
#digitação, exibir os dados (nome, sexo e idade) classificados por sexo 
#(crescente) e depois por idade (decrescente)

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
        if((sexos[i] == "M") and (sexos[j] == "F")):
            auxSexo = sexos[i]
            sexos[i] = sexos[j]
            sexos[j] = auxSexo

            auxIdade = idades[i]
            idades[i] = idades[j]
            idades[j] = auxIdade

            auxNome = nomes[i]
            nomes[i] = nomes[j]
            nomes[j] = auxNome

for i in range(0,3,1):
    print(nomes[i])
    print(sexos[i])
    print(idades[i])

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