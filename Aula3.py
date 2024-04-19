import math
## Aula 3
## https://www.youtube.com/watch?v=Q29XB7TIhBI&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=3

num1 = 5
num2 = 9.9

## type é uma função do python que retorna o tipo de variavel
print(type(num1))
print(type(num2))

x = float(num1)

print(type(x))
print(x)

y = int(num2)

print(type(y))
print(y)


## Variaveis teste
a = 5
b = 6

c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a ** b
i = a // b

print(f"Valor das variaveis teste escolhidas: {a} e {b}")

print(f"{c} soma de {a} com {b}")
print(f"{d} subtração de {a} com {b}")
print(f"{e} multiplicação de {a} com {b}")
print(f"{f} divisão de {a} com {b}")
print(f"{g} resto da divisão de {a} com {b}")
print(f"{h} potência de {a} com {b}")
print(f"{i} divisão inteira de {a} com {b}")


print(abs(-a)) ## retorna o valor absoluto
print(pow(4,4)) ## retorna o valor de 4 elevado a 4
print(max(a,b,num1,num2)) ## retorna o maior
print(min(a,b,num1,num2)) ## retorna o menor
print(round(4.7)) ## arredonda o valor

print (math.floor(4.7)) ## arredonda o valor para baixo.
print (math.ceil(4.7)) ## arredonda o valor para cima.
print (math.sqrt(15)) ## retorna a raiz quadrada