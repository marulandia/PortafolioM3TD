# Inventario de Hilos para Bordado

Descripción

Este programa permite gestionar un inventario de hilos de bordado.
Permite agregar nuevos hilos, buscar por código, usar hilos restando cantidades y verificar si se tienen los hilos necesarios para completar un patrón.

## Funcionalidades

* **Ver inventario:** muestra todos los hilos disponibles con su código, color y cantidad.
* **Agregar hilo:** añade un nuevo hilo o aumenta la cantidad de uno existente.
* **Buscar hilo:** consulta si un hilo está en el inventario.
* **Usar hilo:** descuenta hilos cuando se utilizan en un proyecto.
* **Verificar patrón:** permite ingresar los códigos de un patrón y verificar cuáles hilos faltan.

## Requisitos

* Python 3 instalado en el sistema.

## Ejecución

1. Descargar el archivo `portafolioM3.py`.
2. Abrir una terminal en la carpeta donde está guardado el archivo.
3. Ejecutar el programa con:

   ```bash
   python3 portafolioM3.py
   ```
4. Seguir las instrucciones del menú interactivo.

## Estructura del programa

* **Diccionario `inventario`:** almacena los hilos, donde cada clave es el código del hilo y el valor es otro diccionario con color y cantidad.
* **Funciones:** cada acción del inventario (agregar, buscar, usar, verificar) está modularizada en una función.
* **Menú principal:** un bucle `while` permite que el usuario seleccione las acciones hasta que elija salir.

## Ejemplo de uso

```
=== INVENTARIO DE HILOS ===
1 Ver inventario
2 Agregar hilo
3 Buscar hilo
4 Usar hilo
5 Verificar patrón
6 Salir
```

Seleccionando una opción, el usuario puede gestionar su inventario de manera sencilla.
