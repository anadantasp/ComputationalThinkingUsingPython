#Exercício 7 - Entrar via teclado com o valor de cinco produtos. 
# Após as entradas, digitar um valor referente ao pagamento da somatória destes valores. 
# Calcular e exibir o troco que deverá ser devolvido

a = float(input('Digite o valor do primeiro produto: '))
b = float(input('Digite o valor do segundo produto: '))
c = float(input('Digite o valor do terceiro produto: '))
d = float(input('Digite o valor do quarto produto: '))
e = float(input('Digite o valor do quinto produto: '))

total = a + b + c + d + e;

print('')
print('**************************************')
print('O valor total da compra foi de R${:.2f}'.format(total))
print('**************************************')
print('')

pagamento = float(input('Pagamento: '))

troco = pagamento - total;

print('')
print('**************************************')
print('Troco: R${:.2f}'.format(troco))
print('**************************************')
print('')
