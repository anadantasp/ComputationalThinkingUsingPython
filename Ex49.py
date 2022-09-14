num1 = int(input('Digite o número do início do intervalo: '))
num2 = int(input('Digite o número do final do intervalo: '))

soma = 0

for i in range(num1, num2 + 1, 1):
    soma = soma + i

print('Soma: ', soma)