# Exemplo de print
# Hello World

# Exemplo de input
# Nome e Quantos anos?
# nome = input("Qual é o seu Nome: ")
# saida = "Seu nome é " + nome
# print(saida)
#
# ano = input("Quando você nasceu? ")
# ano = int(ano)
# idade = 2014 - ano
# print("Sua idade é", idade)

# Exemplo de IF/ELSE
# Qual o maior número?
# numero_a = int(input("Digite o número A: "))
# numero_b = int(input("Digite o número B: "))
#
# if numero_a == numero_b:
#     print("Os números são iguais")
# elif numero_a > numero_b:
#     print("O número A é maior")
# else:
#     print("O número B é maior")

# Exemplo de WHILE
# Programa só termina quando eu tou afim
# i = 0
# while i <= 10:
#     if i == 8:
#         i += 2 # i = i + 2
#         continue
#     print(i)
#     i += 2 # i = i + 2

# Exemplo de LIST/FOR
# Lista de frutas
# Lista de números

# valores = ['a', 'b', 1.4, 5]
# valores.append(10)
#
# def print_lista(lista):
#     for i in lista:
#         print(i)

# print_lista(valores)

# Exemplo de Excecao
# Divisão por Zero

numero_a = 10
numero_b = 0
if numero_b == 0:
    raise Exception("Ta errado ai")
# try:
#     print(numero_a / numero_b)
# except Exception as ex:
#     print("Exceção", ex)
