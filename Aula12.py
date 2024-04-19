## Aula 12
## https://www.youtube.com/watch?v=G-kUBX0U8IQ&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=12

import os

## Trabalhando com arquivos (Leitura e Escrita)

## open ("Caminho","r") ## Exemplo

# - r = Ler
# - w = Escrever (cria o arquivo caso o arquivo não exista e sobrescreve caso o arquivo exista) ** importante!
# - a = Acrescentar
# - x = Criar
# - t = Texto
# - r+ = Ler e Escrever

arquivo = open("Aula12/teste2.txt","w")

## print(arquivo.readable()) ## Verifica se é possivel ler o arquivo
## print(arquivo.read()) ## Le o arquivo

## lista = arquivo.readlines()

## print(lista[3])

## print(arquivo.readlines()) ## Le o arquivo linha por linha <**Importante>

arquivo.write("Terraform\n")
arquivo.write("Python3\n")
arquivo.write("+ Alguma linguagem!\n")

arquivo.close() ## Fecha o arquivo



import os
os.remove("Aula12/teste2.txt") ## Remove através do uso da biblioteca os (operation system)

if os.path.exists("Aula12/teste2.txt"):
    os.remove("Aula12/teste2.txt")
else:
    print("Arquivo inexistente")

os.rmdir("Aula13") ## Remove o diretorio