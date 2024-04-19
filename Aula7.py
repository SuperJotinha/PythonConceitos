## Aula 7
## https://www.youtube.com/watch?v=5gqpc-nCq7w

## Funções

def diploma (notas, frequencia): ## Criação da função recebendo 2 argumentos

    if notas >= 5: ## verificação 1
        print ("Aluno tem nota maior ou igual a 5")
    else:
        print ("Aluno tem nota menor que 5")
        exit()

    if frequencia >= 75: ## verificação 2
        print ("Aluno tem frequencia maior ou igual a 75%")
    else:
        print ("Aluno tem frequencia menor que 75%")
        exit()
        
    if notas >= 7 and frequencia >= 75: ## verificação 3 e final
            print("\n")
            print("Aluno esta formado e poderá pegar o diploma!")
            print("\n")    
    else:
            print("nota ou frequencia estiverem abaixo da nota minima")
            print("Aluno não esta formado!")
    

    print(f"As notas e frequencias que foram inseridas foram NOTAS:{notas} e FREQUENCIA:{frequencia}")



print("Programa destinado a fazer a verificação de nota e frequência")
notas = float(input("Insira a sua nota final: "))
frequencia = float(input("Insira a sua frequencia: "))

diploma(notas, frequencia) ## Chamada de função e envio de parametros