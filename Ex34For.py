#Exercício 34 - Exibir a tabuada do número cinco no intervalo de um a dez

num = 5

for i in range(1, 11, 1):
    t = num * i
    print(f'{num} X {i} = {t}')