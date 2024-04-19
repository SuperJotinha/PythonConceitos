## Aula 10
## https://www.youtube.com/watch?v=7uVwpmuw4Yg

## Sets e Dicionários

## Dicionários

mes = {
    "Jan" : "1",
    "Feb" : "2",
    "Mar" : "3",
    "Apr" : "4",
    "May" : "5",
    "Jun" : "6",
    "Jul" : "7",
    "Aug" : "8",
    "Sep" : "9",
    "Oct" : "10",
    "Nov" : "11",
    "Dec" : "12"
}

print(mes["Nov"]) ## Buscando por chaves nesse caso "Nov"
print(mes.get("May", "0")) ## Buscando por chaves nesse caso por "May"
print(mes.get("dfefrfr", "Padrão")) ## Caso o valor que seja passado não exista dentro da lista ele irá retornar o valor "padrão"