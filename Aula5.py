## Aula 5
## https://www.youtube.com/watch?v=i8MCRfA411M&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=5

x = input("Insira qualquer valor aqui: ") ## input pega dados vindos do usuário

nome = input("Digite seu nome: ") ## input pega dados vindos do usuário
idade = int(input(f"Digite agora sua idade, {nome} quantos anos você tem? ")) ## especificar o tipo da variável antes de digitar
nascimento = 2024 - idade

print (f"Seu nome é {nome}, sua idade é {idade} e sua data de nascimento é {nascimento}")

num1 = int(input("Insira um valor a ser somado: "))
num2 = int(input("Insira o segundo valor a ser somado: "))

num3 = num1 + num2

print (f"A soma de {num1} com {num2} foi de: {num3}")