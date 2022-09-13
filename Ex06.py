#Exercício 6 - Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. Calcular e exibir o valor correspondente em Reais (R$).

cotacao = float(input('Informe o valor da cotação do dólar de hoje: '))
valor = float(input('Informe o valor da quantia em dólares: '))

total = valor * cotacao;

print('O valor total em reais é R${:.2f}'.format(total))