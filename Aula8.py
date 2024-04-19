## Aula 8
## https://www.youtube.com/watch?v=LvzbitCIURg&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=8

# Funções Or And

def cozinhaComida (Fome, Sede):
    if Fome == True:
        print("Vou a cozinha comer alguma coisa")
    else:
        print("Vou ficar de boas e continuar no meu quarto!")

    if Sede == True:
        print("Vou a cozinha beber alguma coisa")
    else:
        print("Vou ficar de boa e continuar no meu quarto!")


    if Fome and Sede == True: ## Condição AND
        print("Vou a cozinha beber e comer alguma coisa")
    else:
        print("Vou ficar de boa e continuar no meu quarto!")

    if Fome or Sede == True: ## Condição OR 
        print("Vou a cozinha beber e comer alguma coisa")
    else:
        print("Vou ficar de boa e continuar no meu quarto!")

    if not(Fome) == True: ## Condição NOT
        print("Vou ficar de boa e continuar no meu quarto!")
    else:
        print("Vou a cozinha beber e comer alguma coisa")
    

Fome = str(input("Tem fome, S ou N ? :"))
Sede = str(input("Você tem sede, S ou N ? :"))

Fome = Fome.upper() ## Transforma todas as letras em maiúsculas
Sede = Sede.upper() ## Transforma todas as letras em maiúsculas

print(Fome)
print(Sede)

if Sede == "S":
    Sede = True
else:
    Sede = False

if Fome == "S":
    Fome = True
else:
    Fome = False


print(type(Sede)) ## Verifica o tipo de variável
print(type(Fome)) ## Verifica o tipo de variável

cozinhaComida(Fome, Sede)
print("Programa encerrado!")