#weazelda

inventario = []
contador_max_items = 0

def mostrar_menu():
    print("="*12, "MENU", "="*12)
    print("1: Agregar objeto al inventario")
    print("2: Equipar objeto del inventario")
    print("3: Verificar estados de combate")
    print("4: Ver objetos del inventario")
    print("5: Ver objetos equipados")
    print("6: Salir")
    print("="*30)

def leer_opcion():
    while True:
        try:
            opt = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Error: Debes ingresar un numero entero valido")
            continue
        
        if opt < 0 or opt > 6:
            print("Error: Debes ingresar un numero entero entre 1 a 6")
            continue

        return opt
    
def validar_nombre_item(nombre):
    return len(nombre.strip()) > 0

def agregar_item():
    global contador_max_items

    while True:
        agregar_item = input("¿Que item deseas agregar?: ")

        if not validar_nombre_item(agregar_item):
            print("Error: El nombre del item no puede quedar vacio ni espacios en blanco")
            continue

        if agregar_item.isdigit():
            print("Error: El nombre del item no puede contener numeros")
            continue

        if contador_max_items == 4:
            print("Error: Se ha alcanzado la cantidad maxima en el inventario")
            return
        else:
            contador_max_items += 1
            nuevo_item = [agregar_item]
            inventario.append(nuevo_item)
            print(f"El item '{agregar_item}' fue añadido correctamente al inventario")

def equipar_item():
    if len(inventario) == 0:
        print("Error: No hay ningun objeto en el inventario para equipar")
        return
    
    seleccion_item = input("Ingresa el nombre del item que deseas equipar: ")
    