
#for: comando cual va ejecutar un cierto numeros de veces una variable segun una secuencia
#variable: variable cual va a recorrer la secuencia una vez por cada elemento que tenga la secuencia
#in: que secuencia se va a recorrer
#secuencia: lista, tupla, string o rango de numeros cual contendra lo que se va iterar

for i in range(5):
    print(i)

#range(): se usa para contar, en este caso va generar 5 numeros, partiendo del 0
#print(i): va recorrer la secuencia range(5), range va a generar 5 numeros, e "i" va a imprimir los 5 numeros generados, que seran del 0 al 4

#listas

frutas = ["manzana", "plátano", "cereza"]
for fruta in frutas:
    print(fruta)

#la variable "fruta" recorre la secuencia "frutas", la cual imprime una vez por los elementos que tenga la lista

#strings

for letra in "Pikachu":
    print(letra)

#la variable "letra" recorre la secuencia "Pikachu", cual imprimira cada letra del string

#diccionarios

pokemon = {"nombre": "Charmander", "tipo": "fuego", "nivel": 5}

for clave, valor in pokemon.items():
    print(clave, "->", valor)
