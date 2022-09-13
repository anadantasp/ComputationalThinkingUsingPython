#Exercício 22 - Exibir o seguinte seletor de opções e em função de uma escolha, 
#solicitar os dados necessários para o cálculo da respectiva área. Enviar mensagem 
# de erro se o usuário escolher uma opção inexistente.
#
#Encerrar o programa somente quando selecionada a opção de finalização. (Fazer esse 
# exercício utilizando If..Else e/ou Case)
#
#1 – Triângulo
#2 – Quadrado
#3 – Retângulo
#4 – Círculo
#5 – Fim de processo

print("MENU")
print("1 - Triângulo")
print("2 - Quadrado")
print("3 - Retângulo")
print("4 - Círculo")
print("5 - Encerrar programa")
opcao = int(input('Digite o número da figura que deseja calcular a área: '))

if(opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5):
    print('OPÇÃO INVÁLIDA')
else:
    if opcao == 1:
        base = int(input('Digite a base do triângulo: '))
        altura = int(input('Digite a altura do triângulo: '))
        area = ((base * altura) / 2)
        print(f'Área: {area}')
    elif opcao == 2:
        lado = int(input('Digite o valor do lado do quadrado: '))
        area = lado * lado
        print(f'Área: {area}')
    elif(opcao == 3):
        base = int(input('Digite a base do retângulo: '))
        altura = int(input('Digite a altura do retângulo: '))
        area = base * altura
        print(f'Área: {area}')
    elif(opcao == 4):
        raio = int(input('Digite o valor do raio do círculo: '))
        area = 3,14 * (raio * raio)
        print(f'Área: {area}')
    else:
        print('Encerrando o programa')

