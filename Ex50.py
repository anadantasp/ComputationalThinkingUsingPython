num1 = int(input('Digite o número do início do intervalo: '))
num2 = int(input('Digite o número do final do intervalo: '))

for i in range(num1, num2 + 1, 1):
    if(i % 2 == 0 and i > 10):
        print(f'{i}, ')