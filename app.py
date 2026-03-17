"""
Aplicación Principal para la Gestión de Inventario.

Este script proporciona una interfaz de línea de comandos (CLI) para que un usuario
pueda interactuar con el sistema de inventario. Permite realizar operaciones
básicas como agregar, mostrar, buscar, actualizar, y eliminar productos,
además de visualizar estadísticas del inventario.
"""

# Importamos las funciones del módulo de servicios
import servicios as srv
import archivos as arch

def mostrar_menu():
    """Imprime el menú de opciones en la consola."""
    print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---\n")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Mostrar estadísticas del inventario")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")
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
        print(f"  - Unidades totales: {stats['unidades_totales']}")
        print(f"  - Valor total del inventario: ${stats['valor_total']:.2f}")
        print(f"  - Producto más caro: {stats['producto_mas_caro']['nombre']} (${stats['producto_mas_caro']['precio']:.2f})")
        print(f"  - Producto con mayor stock: {stats['producto_mayor_stock']['nombre']} ({stats['producto_mayor_stock']['cantidad']} unidades)")
    else:
        print("El inventario está vacío, no se pueden calcular estadísticas.")

def ejecutar_guardar_inventario(inventario):
    """Solicita ruta y guarda el inventario."""
    print("\n-> Guardar Inventario")
    ruta = input("Introduce la ruta/nombre del archivo (ej. inventario.csv): ")
    arch.guardar_csv(inventario, ruta)

def ejecutar_cargar_inventario(inventario):
    """Gestiona la carga de inventario desde CSV."""
    print("\n-> Cargar Inventario")
    ruta = input("Introduce la ruta del archivo CSV a cargar: ")
    
    cargados, invalidos = arch.cargar_csv(ruta)
    
    if cargados is None:
        return # Error crítico al abrir/leer archivo

    print(f"\nProductos válidos detectados: {len(cargados)}")
    if invalidos > 0:
        print(f"Filas inválidas omitidas: {invalidos}")

    if not cargados:
        print("No se encontraron productos válidos para importar.")
        return

    while True:
        resp = input("¿Sobrescribir inventario actual? (S/N): ").lower()
        if resp in ['s', 'n']:
            break
    
    accion = ""
    if resp == 's':
        inventario.clear()
        inventario.update(cargados)
        accion = "Reemplazo total"
    else:
        accion = "Fusión"
        for nombre, datos in cargados.items():
            if nombre in inventario:
                inventario[nombre]['cantidad'] += datos['cantidad']
                inventario[nombre]['precio'] = datos['precio'] # Actualiza precio al nuevo
            else:
                inventario[nombre] = datos
    
    print(f"\nOperación completada: {accion}.")
    print(f"Estado actual: {len(inventario)} tipos de productos en inventario.")

def main():
    """Función principal que ejecuta el bucle de la aplicación."""
    
    # El inventario se define como un diccionario vacío al inicio.
    inventario = {}
    
    # Bucle principal de la aplicación
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-9): ")

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
            ejecutar_guardar_inventario(inventario)
        elif opcion == '8':
            ejecutar_cargar_inventario(inventario)
        elif opcion == '9':
            print("\nGracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 9.")
        
        # Pausa para que el usuario pueda leer la salida antes de mostrar el menú de nuevo
        input("\nPulsa Enter para continuar...")


# Punto de entrada del script: si se ejecuta este archivo, se llama a main()
if __name__ == "__main__":
    main()
