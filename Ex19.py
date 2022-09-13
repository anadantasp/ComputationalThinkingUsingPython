#Exercício 19 - Uma escola com cursos em regime semestral, realiza duas avaliações 
# durante o semestre e calcula a média do aluno, da seguinte maneira:
#
#MEDIA = (P1 + 2.P2) / 3
#
#Fazer um programa para entrar via teclado com os valores das notas (P1 e P2) e 
#calcular a média. Exibir a situação final do aluno (“Aprovado ou Reprovado”), 
#sabendo que a média de aprovação é igual a cinco.

p1 = float(input('Entre com a primeira nota: '))
p2 = float(input('Entre com a primeira nota: '))

media = (p1 + 2 * p2) / 3

if(media >= 5):
	print('APROVADO')
	print('Média {:.1f}'.format(media))
else:
	print("REPROVADO")
	print('Média {:.1f}'.format(media))