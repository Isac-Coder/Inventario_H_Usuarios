"""
Aplicación Principal para la Gestión de Inventario.

Este script proporciona una interfaz de línea de comandos (CLI) para que un usuario
pueda interactuar con el sistema de inventario. Permite realizar operaciones
básicas como agregar, mostrar, buscar, actualizar, y eliminar productos,
además de visualizar estadísticas del inventario.
"""

# Importamos las funciones del módulo de servicios
import servicios as srv

def mostrar_menu():
    """Imprime el menú de opciones en la consola."""
    print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Mostrar estadísticas del inventario")
    print("7. Salir")
    print("------------------------------------")

def ejecutar_agregar_producto(inventario):
    """Solicita datos al usuario y agrega un producto."""
    print("\n-> Agregar Nuevo Producto")
    try:
        nombre = input("Introduce el nombre del producto: ")
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad del producto: "))
        
        # Llama a la función del módulo de servicios
        srv.agregar_producto(inventario, nombre, precio, cantidad)

    except ValueError:
        print("\nError: El precio y la cantidad deben ser números.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")


def ejecutar_buscar_producto(inventario):
    """Solicita nombre y busca un producto."""
    print("\n-> Buscar Producto")
    nombre = input("Introduce el nombre del producto que deseas buscar: ")
    producto = srv.buscar_producto(inventario, nombre)
    if producto:
        print("\n--- Producto Encontrado ---")
        print(f"Nombre: {nombre.strip().title()}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        print("---------------------------")
    else:
        print(f"\nEl producto '{nombre.strip().title()}' no se encontró en el inventario.")

def ejecutar_actualizar_producto(inventario):
    """Solicita datos y actualiza un producto."""
    print("\n-> Actualizar Producto")
    nombre = input("Introduce el nombre del producto a actualizar: ")
    
    # Primero, verificar si el producto existe
    if srv.buscar_producto(inventario, nombre) is None:
        print(f"\nError: El producto '{nombre.strip().title()}' no se encontró.")
        return

    nuevo_precio = None
    nueva_cantidad = None

    # Preguntar por el nuevo precio
    resp_precio = input("¿Deseas actualizar el precio? (s/n): ").lower()
    if resp_precio == 's':
        try:
            nuevo_precio = float(input("Introduce el nuevo precio: "))
        except ValueError:
            print("Entrada inválida para el precio. No se actualizará.")

    # Preguntar por la nueva cantidad
    resp_cantidad = input("¿Deseas actualizar la cantidad? (s/n): ").lower()
    if resp_cantidad == 's':
        try:
            nueva_cantidad = int(input("Introduce la nueva cantidad: "))
        except ValueError:
            print("Entrada inválida para la cantidad. No se actualizará.")
    
    # Llama a la función de servicio para actualizar
    srv.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

def ejecutar_eliminar_producto(inventario):
    """Solicita nombre y elimina un producto."""
    print("\n-> Eliminar Producto")
    nombre = input("Introduce el nombre del producto a eliminar: ")
    srv.eliminar_producto(inventario, nombre)


def ejecutar_mostrar_estadisticas(inventario):
    """Calcula y muestra las estadísticas del inventario."""
    print("\n-> Estadísticas del Inventario")
    stats = srv.calcular_estadisticas(inventario)
    if stats:
        print(f"  - Número total de tipos de productos: {stats['numero_tipos_productos']}")
        print(f"  - Cantidad total de unidades: {stats['cantidad_total_unidades']}")
        print(f"  - Valor total del inventario: ${stats['valor_total_inventario']:.2f}")
        print(f"  - Precio promedio ponderado: ${stats['precio_promedio_ponderado']:.2f}")
        print(f"  - Producto más caro: {stats['producto_mas_caro']['nombre']} (${stats['producto_mas_caro']['precio']:.2f})")
        print(f"  - Producto más barato: {stats['producto_mas_barato']['nombre']} (${stats['producto_mas_barato']['precio']:.2f})")
    else:
        print("El inventario está vacío, no se pueden calcular estadísticas.")


def main():
    """Función principal que ejecuta el bucle de la aplicación."""
    
    # El inventario se define como un diccionario vacío al inicio.
    inventario = {}
    
    # Bucle principal de la aplicación
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == '1':
            ejecutar_agregar_producto(inventario)
        elif opcion == '2':
            srv.mostrar_inventario(inventario)
        elif opcion == '3':
            ejecutar_buscar_producto(inventario)
        elif opcion == '4':
            ejecutar_actualizar_producto(inventario)
        elif opcion == '5':
            ejecutar_eliminar_producto(inventario)
        elif opcion == '6':
            ejecutar_mostrar_estadisticas(inventario)
        elif opcion == '7':
            print("\nGracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 7.")
        
        # Pausa para que el usuario pueda leer la salida antes de mostrar el menú de nuevo
        input("\nPulsa Enter para continuar...")


# Punto de entrada del script: si se ejecuta este archivo, se llama a main()
if __name__ == "__main__":
    main()
