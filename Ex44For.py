#Exercício 44 -Entrar via teclado com dez valores positivos. Consistir a digitação e enviar mensagem de erro, se necessário. 
#Após a digitação, exibir:
#a) O maior valor;
#b) A soma dos valores;
#c) A média aritmética dos valores;

soma = 0

for i in range(1, 11, 1):
    num = int(input('Digite um número: '))

    while(num < 0):
        print('Opa! Não pode números negativos!')
        num = int(input('Digite outro número: '))
    
    if(i == 1):
        maior = num
    else:
        if(num > maior):
            maior = num

    soma = soma + num

media = soma / 10

print('O maior valor: ', maior)
print('Soma dos valores: ', soma)
print('Média: ', media)

        

