#Exercício 33 - Entrar via teclado com o sexo de determinado usuário, aceitar somente 
#“F” ou “M” como respostas válidas

sexo = input('Informe o seu gênero(F/M): ').upper()

while(sexo != "F" and sexo != "M"):
    print('Seguir padrão F/M')
    sexo = input('Informe o seu gênero(F/M): ').upper()

print('Gênero: ', sexo)
