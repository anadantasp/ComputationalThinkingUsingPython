#Exercício 55 - Armazenar um máximo de 20 valores em um vetor. A quantidade de valores a serem 
#armazenados será escolhida pelo usuário. Enviar mensagem de erro, caso a quantidade de valores 
#escolhida esteja fora da faixa possível e solicitar a quantidade novamente. Após a digitação 
#dos valores, criar uma rotina de consulta, onde o usuário digita um número e o programa exibe 
#em qual posição do vetor este número está localizado. Se o número não for encontrado, enviar 
#mensagem “Valor não encontrado!”. Perguntar ao usuário se deseja ou não fazer uma nova consulta,
#consistir a resposta e encerrar o programa em caso negativo.

quant = int(input('Digite a quantidade de números que deseja armazenar: ' ))

while(quant > 20):
    print('A quantidade máxima permitida é 20 números')
    quant = int(input('Digite a quantidade de números que deseja armazenar: ' ))

numeros = []

for i in range(0,quant,1):
    num = int(input('Digite um número: '))
    numeros.append(num)

escolha = 'S'

while(escolha == 'S'):

    x = int(input('Gostaria de saber a posição de qual número?'))

    pos = -1

    for i in range(0, quant, 1):
        if(numeros[i] == x):
            pos = i

    if(pos != -1):
        print(f'O número {x} esta na posição {pos}')
    else:
        print('Valor não encontrado!')

    escolha = input('Deseja fazer uma nova consulta?(S/N)').upper()

    while(escolha != 'S' and escolha != 'N'):
        print('Seguir padrão S/N')
        escolha = input('Deseja fazer uma nova consulta?(S/N)').upper()


