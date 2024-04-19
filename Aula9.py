## Aula 9
## https://www.youtube.com/watch?v=LvzbitCIURg&t=1s

## Loops (While & For)

## While 
    ## Aqui há a necessidade de sempre somar x = x + 1 para que o loop seja executado.
x = 1
while (x <= 10):
    print(f"{x} ainda é menor que 10")
    if x == 9:
        x = x + 1
        print(f"{x} Agora X é igual a 10")
        break
    else:
        x = x + 1

## For (Uma curiosidade é que o valor que é rodado no looping é criado dentro do looping nesse caso a baixo!)
        ## Dentro do For não há a necessidade de colocar x = x + 1 o próprio looping soma com a variável.
for y in range(10):
    print(f"{y} ainda é menor que 10")
    if y == 9:
        print(f"{y} agora é igual a 10")
        break
