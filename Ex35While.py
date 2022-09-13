#Entrar via teclado com um valor qualquer. Travar a digitação, no sentido de aceitar 
#somente valores positivos. Após a digitação, exibir a tabuada do valor solicitado, 
#no intervalo de um a dez

num = int(input('Digite um número que deseja a tabuada: '))

while(num <= 0):
    print('O número não pode ser negativo!')
    num = int(input('Digite um número que deseja a tabuada: '))

i = 1

while(i <= 10):
    t = num * i 
    print(f'{num} X {i} = {t}')
    i = i + 1
