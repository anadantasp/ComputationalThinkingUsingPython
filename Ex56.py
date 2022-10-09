# Exercício 56 - Armazenar o nome e idade de cem pessoas. Após a digitação,
# exibir os dados (nome e idade) de todas as pessoas.


nomes = []
idades = []

for i in range(0,5,1):
    nome = input('Digite o nome: ')
    nomes.append(nome)
    idade = int(input('Digite a idade: '))
    idades.append(idade)

for i in range(0,5,1):
    print('Nome: ', nomes[i])
    print('Idade: ', idades[i])