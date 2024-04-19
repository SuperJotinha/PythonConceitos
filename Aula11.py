## Aula 11
## https://www.youtube.com/watch?v=U0n7CZXGZGE&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=11

## Try, Except e Finally

try: ## Tenta executar o que estiver dentro do bloco
    x = int(input("Insira um valor INTEIRO:")) 
    print(f"O valor inserido foi -> {x}")
except ZeroDivisionError: ## Caso de erro
    print("Número inserido não divisível por ZERO!") 
except ValueError: ## Caso de erro
    print("Valor inserido não é válido!")
except: ## Caso de erro
    print("Erro inesperado!")
finally: ## Sempre
    print("Sempre aparece no final do código!")