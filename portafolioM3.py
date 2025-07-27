# Acá estoy probando funcionalidades del proyecto de M2

# El inventario es un diccionario con códigos de hilos como clave, y otro diccionario interno con "color" y "cantidad"
#Para cada patrón de bordado tendría que tener un inventario de hilos como diccionario.
#La clave son los códigos de los hilos

inventario = {
    "159": {"color": "Gray Blue-LT", "cantidad": 1},
    "300": {"color": "Mahogany-VY DK", "cantidad": 1},
    "304": {"color": "Christmas Red-MD", "cantidad": 1},
    "310": {"color": "Black", "cantidad": 11},
    "317": {"color": "Pewter Gray", "cantidad": 1},
    "318": {"color": "Steel Gray-LT", "cantidad": 1},
    "413": {"color": "Pewter Gray-DK", "cantidad": 1},
    "414": {"color": "Steel Gray-DK", "cantidad": 1},
    "434": {"color": "Brown-LT", "cantidad": 1},
    "435": {"color": "Brown-VY LT", "cantidad": 1},
    "436": {"color": "Tan", "cantidad": 1},
    "610": {"color": "Drab Brown-DK", "cantidad": 1},
    "612": {"color": "Drab Brown-LT", "cantidad": 2},
    "700": {"color": "Christmas Green-BRT", "cantidad": 1},
    "738": {"color": "Tan-VY LT", "cantidad": 1},
    "739": {"color": "Tan-UL VY LT", "cantidad": 1},
    "801": {"color": "Coffee Brown-DK", "cantidad": 1},
    "803": {"color": "Baby Blue-UL VY DK", "cantidad": 1},
    "814": {"color": "Garnet-DK", "cantidad": 1},
    "815": {"color": "Garnet-MD", "cantidad": 1},
    "820": {"color": "Royal Blue-VY DK", "cantidad": 1},
    "823": {"color": "Navy Blue-DK", "cantidad": 1},
    "839": {"color": "Beige Brown-DK", "cantidad": 1},
    "840": {"color": "Beige Brown-MD", "cantidad": 1},
    "890": {"color": "Pistachio Green-UL DK", "cantidad": 1},
    "900": {"color": "Burnt Orange-DK", "cantidad": 1},
    "919": {"color": "Red Copper", "cantidad": 1},
    "920": {"color": "Copper-MD", "cantidad": 1},
    "921": {"color": "Copper", "cantidad": 1},
    "922": {"color": "Copper-LT", "cantidad": 1},
    "938": {"color": "Coffee Brown-UL DK", "cantidad": 1},
    "951": {"color": "Tawny-LT", "cantidad": 13},
    "977": {"color": "Golden Brown-LT", "cantidad": 2},
    "995": {"color": "Electric Blue-DK", "cantidad": 1},
    "996": {"color": "Electric Blue-MD", "cantidad": 1},
    "3031": {"color": "Mocha Brown-VY DK", "cantidad": 1},
    "3046": {"color": "Yellow Beige-MD", "cantidad": 1},
    "3371": {"color": "Black Brown", "cantidad": 2},
    "3770": {"color": "Tawny-VY LT", "cantidad": 1},
    "3776": {"color": "Mahogany-LT", "cantidad": 1},
    "3821": {"color": "Straw", "cantidad": 1},
    "3822": {"color": "Straw-LT", "cantidad": 1},
    "3827": {"color": "Golden Brown-Pale", "cantidad": 1},
    "3828": {"color": "Hazelnut Brown", "cantidad": 1},
    "3830": {"color": "Terra Cotta-MD", "cantidad": 1},
    "3842": {"color": "Wedgewood-DK", "cantidad": 1},
    "3844": {"color": "Bright Turquoise-DK", "cantidad": 1},
    "3855": {"color": "Autumn Gold-LT", "cantidad": 1},
    "3862": {"color": "Mocha Beige-DK", "cantidad": 1}
}


#Primero, quiero mostrar los hilos del inventario
def mostrar_inventario():
    if not inventario:
        print("\nNo hay hilos en el inventario.\n")
    else:
        print("\nInventario actual:")
        for codigo, datos in inventario.items():
            print(f"Código: {codigo} | Color: {datos['color']} | Cantidad: {datos['cantidad']}")
        

#Esta función me permite agregar un nuevo hilo al inventario o aumentar la cantidad de uno existente.
def agregar_hilo():
    codigo = input("Ingrese el código del hilo (ej. 310): ").strip()
    color = input("Ingrese el nombre del color: ").capitalize()
    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("La cantidad debe ser un número.")
        return

    if codigo in inventario:
        inventario[codigo]["cantidad"] += cantidad
        print(f"Se sumaron {cantidad} hilos al código {codigo}. Total ahora: {inventario[codigo]['cantidad']}")
    else:
        inventario[codigo] = {"color": color, "cantidad": cantidad}
        print(f"Hilo {codigo} - {color} agregado con {cantidad} unidades.")

#Con esta función puedo buscar un hilo por código y que me muestre su información.
def buscar_hilo():
    codigo = input("Ingrese el código del hilo a buscar: ").strip()
    if codigo in inventario:
        datos = inventario[codigo]
        print(f"Código: {codigo} | Color: {datos['color']} | Cantidad: {datos['cantidad']}")
    else:
        print("Ese hilo no está en el inventario.")

#Con esta función puedo restar esta cantidad de un hilo cuando se usa en un proyecto.
def usar_hilo():
    codigo = input("Ingrese el código del hilo a usar: ").strip()
    if codigo in inventario:
        try:
            cantidad = int(input("¿Cuántos hilos usaste?: "))
        except ValueError:
            print("La cantidad debe ser un número.")
            return

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
        elif cantidad > inventario[codigo]["cantidad"]:
            print("No tienes suficientes hilos de ese color.")
        else:
            inventario[codigo]["cantidad"] -= cantidad
            print(f"Se usaron {cantidad} hilos de {codigo}. Quedan {inventario[codigo]['cantidad']}.")
    else:
        print("Ese hilo no está en el inventario.")

#Cuándo ya tengo un patrón desterminado, con esta función puedo comprobar si tengo todos los hilos necesarios para un patrón.
def verificar_patron():
    print("\nVerificación de patrón")
    print("Ingrese los códigos del patrón separados por coma (ej. 310,321,415):")
    codigos = input("👉 ").split(",")

    faltantes = []
    for codigo in codigos:
        codigo = codigo.strip()
        if codigo not in inventario or inventario[codigo]["cantidad"] == 0:
            faltantes.append(codigo)

    if not faltantes:
        print("✅ Tienes todos los hilos para este patrón.")
    else:
        print("⚠️ Te faltan estos hilos:", ", ".join(faltantes))

# Función principal del menú para interactuar con el usuario y manejar las opciones del inventario.

def menu():
    while True:
        print("""
=== INVENTARIO DE HILOS ==
1 Ver inventario
2 Agregar hilo
3 Buscar hilo
4 Usar hilo
5 Verificar patrón
6 Salir
""")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_hilo()
        elif opcion == "3":
            buscar_hilo()
        elif opcion == "4":
            usar_hilo()
        elif opcion == "5":
            verificar_patron()
        elif opcion == "6":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()