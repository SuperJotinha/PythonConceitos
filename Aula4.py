## Aula 4
## https://www.youtube.com/watch?v=QpEM1cRz1LQ&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=4

string = "o que é String? String é qualquer texto dentro de paresenteses"
print(string)

x = "você pode concatenar Strings"

print(f"Dessa maneira utilizando o f antes do texto {x}") ## f antes do texto você pode concatenar Strings

x = "João Pedro"

print (x.upper()) ## Transforma a string em caixa alta
print (x.lower()) ## Transforma a string em caixa baixa
print (x.capitalize()) ## Transforma a primeira letra da string em caixa alta
print (x.title()) ## Transforma a primeira letra de cada palavra em caixa alta
print (x.islower()) ## Verifica se a string é minuscula
print (x.isupper()) ## Verifica se a string é maiuscula
print (x.strip()) ## Remove os espacos em branco da string, lembrando que o strip funciona para o lado esquerdo e direito.(Começo e final de string)
print (len(x)) ## Retorna o tamanho da string