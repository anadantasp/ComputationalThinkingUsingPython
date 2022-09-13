#Exercício 21 - Entrar via teclado com dois valores quaisquer. Após a digitação, 
# exibir um seletor de opções (“menu”) com as seguintes opções: 
# (Fazer esse exercício utilizando If..Else e/ou Case)
#
#1 – Multiplicação
#2 – Adição
#3 – Divisão
#4 – Subtração
#5 – Fim de processo (sair do programa)
#
#Solicitar uma opção por parte do usuário, verificar se é ou não uma opção válida 
# (letras ou números) e processar a respectiva operação. Enviar mensagem de erro se 
# a opção escolhida não existir no seletor.
#
#Encerrar o programa somente quando o usuário escolher a opção de finalização. 
# Repare que a opção de número três é de divisão e o programa deverá enviar mensagem 
# de erro, (somente nesta opção) se o denominador for zero.

num1 = float(input('Entre com o primeiro número: '))
num2 = float(input('Entre com o segundo número: '))

print("MENU")
print("1 - Multiplicação")
print("2 - Adição")
print("3 - Divisão")
print("4 - Subtração")
print("5 - Encerrar programa")
opcao = int(input('Digite o número da opção desejada: '))

if(opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5):
    print('OPÇÃO INVÁLIDA')
else:
    if opcao == 1:
        res = num1 * num2
        print(f'{num1} X {num2} = {res}')
		
    elif opcao == 2:
        res = num1 + num2
        print(f'{num1} + {num2} = {res}')
    elif(opcao == 3):
        if(num2 != 0):
            res = num1 / num2
            print(f'{num1} / {num2} = {res}')
        else: 
            print('[ERRO] O denominador tem que ser diferente de zero!')
    elif(opcao == 4):
        res = num1 - num2
        print(f'{num1} - {num2} = {res}')
    else:
        print('Encerrando o programa')


