#Exercício 37 - Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. 
#Entre as tabuadas, solicitar que o usuário pressione uma tecla

i = 1

while(i <= 20):
    j = 1
    while(j <= 10):
        res = i * j
        print(f'{i} X {j} = {res}')
        j = j + 1
    print('')
    print('Aperte enter para continuar')
    input('')
    i = i + 1
