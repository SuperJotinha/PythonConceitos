## Aula 6
## https://www.youtube.com/watch?v=5gqpc-nCq7w&list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ&index=6

Gostos = ["Futebol", "Valorant", "Santos", "Programação", "GoT"] ## Lista dentro com valores
##            0         1            2          3           4
##            -5        -4           -3         -2          -1

print (Gostos[2])
print (Gostos[-3])
print (Gostos[2:4])

Gostos.extend(["CTF","Hacking"]) ## Acrescenta valores na lista
print (Gostos)

Gostos.remove("Hacking") ## Remove valores da lista
print (Gostos)

Gostos.append("Calor") ## Acrescenta valores na lista sem a necessidade de abrir colchetes 

Gostos.insert(0, "Casa") ## Acrescenta valores na lista podendo decidir aos será a posição do que será inserido

Gostos.pop() ## Remove o último elemento da lista

Gostos.remove("CTF") ## Remove o elemento da lista

## Gostos.sort() ## Ordena a lista

## Gostos.reverse() ## Inverte a lista

print(Gostos.index("Futebol"))

print (Gostos)

Gostos.clear() ## Limpa a lista