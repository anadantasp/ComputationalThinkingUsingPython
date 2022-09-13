#Exercício 37 - Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. 
#Entre as tabuadas, solicitar que o usuário pressione uma tecla

for i in range(1, 21, 1):
    for j in range(1, 11, 1):
        res = i * j
        print(f'{i} X {j} = {res}')
    print('')
    print('Aperte enter para continuar')
    input('')
