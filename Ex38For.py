#Exercício 38 - Exibir a soma dos números inteiros positivos do intervalo de um a cem.

soma = 0

for i in range(1, 101, 1):
    soma = soma + i

print('A soma dos números inteiros num intervalo de 1 a 100 é ', soma)
