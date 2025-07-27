# Acá estoy probando funcionalidades del proyecto de M2

# El inventario es un diccionario con códigos de hilos como clave, y otro diccionario interno con "color" y "cantidad"
#Para cada patrón de bordado tendría que tener un inventario de hilos como diccionario.
#La clave son los códigos de los hilos

inventario = {
    "310": {"color": "Negro", "cantidad": 5},
    "321": {"color": "Rojo", "cantidad": 3},
    "415": {"color": "Gris", "cantidad": 2}
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