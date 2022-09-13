#Exercício 20 - Uma escola com cursos em regime semestral realiza duas avaliações 
#durante o semestre e calcula a média do aluno, da seguinte maneira:
#
#MEDIA = (P1 + 2.P2) / 3
#
#Fazer um programa para entrar via teclado com o valor da primeira nota (P1) e o 
#programa deverá calcular e exibir quanto o aluno precisa tirar na segunda nota 
#minimamente (P2) para ser aprovado, sabendo que a média de aprovação é igual a cinco.

media = 5
p1 = float(input('Entre com a primeira nota: '))

p2 = (3 * media - p1) / 2

print('Nota mínima na P2 para aprovação: {%.1f}'.format(p2))
