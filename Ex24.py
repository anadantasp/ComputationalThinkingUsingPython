#Exercício 24 - Faça um algoritmo que leia o nome, o sexo e o estado civil de uma 
# pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de 
# casada (anos).

nome = input('Digite o seu nome: ')
sexo = input('Digite o seu gênero: ')
civil = input('Digite o seu estado civil: ')

if(sexo.upper() == "F" and civil.upper() == "CASADA"):
    anos = int(input('Há quantos anos você está casada? '))