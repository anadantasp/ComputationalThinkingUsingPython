resposta = 'S'

while(resposta == 'S'):

    num = int(input('Deseja calcular o fatorial de qual número? '))

    while(num <= 0):
        print('Opa! Não pode número negativo!')
        num = int(input('Deseja calcular o fatorial de qual número? '))


    for i in range(num - 1, 0, -1):
        resultado = num * i
        num = resultado
        
        
    print('Fatorial: ', resultado)
    resposta = input('Deseja uma nova execução do programa?(S/N) ').upper()

    while(resposta != 'S' and resposta != 'N'):
        print('Seguir padrão de resposta S/N')
        resposta = input('Deseja uma nova execução do programa?(S/N) ').upper()


