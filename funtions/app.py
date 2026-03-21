# Importamos las funciones del módulo de servicios
import funtions.servicios as srv
import funtions.archivos as arch
from funtions.extras import *

def mostrar_menu():
    """Imprime el menú de opciones en la consola y retorna la elección del usuario."""
    print(f"{AMARILLO}\n--- MENÚ DE GESTIÓN DE INVENTARIO ---\n")
    print(f"{BLANCO}1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Mostrar estadísticas del inventario")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print(f"9.{ROJO} Salir{BLANCO}")
    print("------------------------------------")
    opcion = input("Selecciona una opción: ")
    return opcion

def ejecutar_agregar_producto(inventario):
    """Solicita datos al usuario y agrega un producto."""
    print(f"{AMARILLO}\n-> Agregar Nuevo Producto\n")
    try:
        nombre = input(f"Introduce el nombre del producto:\n{BLANCO}# ")
        precio = float(input(f"Introduce el precio del producto:\n# "))
        cantidad = int(input(f"Introduce la cantidad del producto:\n# "))
        
        # Llama a la función del módulo de servicios
        srv.agregar_producto(inventario, nombre, precio, cantidad)

    except ValueError:
        print(f"{ROJO}\nError: El precio y la cantidad deben ser números.")
    except Exception as e:
        print(f"{ROJO}\nOcurrió un error inesperado: {e}")


def ejecutar_buscar_producto(inventario):
    """Solicita nombre y busca un producto."""
    print(f"{AMARILLO}\n-> Buscar Producto")
    nombre = input(f"{VERDE}Introduce el nombre del producto que deseas buscar:\n{BLANCO}# ")
    producto = srv.buscar_producto(inventario, nombre)
    if producto:
        print(f"{VERDE}\n--- Producto Encontrado ---")
        print(f"{BLANCO}Nombre: {nombre.strip().title()}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        print("---------------------------")
    else:
        print(f"{ROJO}\nEl producto '{nombre.strip().title()}' no se encontró en el inventario.")

def ejecutar_actualizar_producto(inventario):
    """Solicita datos y actualiza un producto."""
    print(f"{AMARILLO}\n-> Actualizar Producto")
    nombre = input(f"{VERDE}Introduce el nombre del producto a actualizar:\n{BLANCO}# ")
    
    # Primero, verificar si el producto existe
    if srv.buscar_producto(inventario, nombre) is None:
        print(f"{ROJO}\nError: El producto '{nombre.strip().title()}' no se encontró.")
        return

    nuevo_precio = None
    nueva_cantidad = None

    # Preguntar por el nuevo precio
    resp_precio = input(f"{AMARILLO}¿Deseas actualizar el precio? (s/n):\n{BLANCO}# ").lower()
    if resp_precio == 's':
        try:
            nuevo_precio = float(input(f"{AMARILLO}Introduce el nuevo precio:\n{BLANCO}# "))
        except ValueError:
            print(f"{ROJO}Entrada inválida para el precio. No se actualizará.")

    # Preguntar por la nueva cantidad
    resp_cantidad = input(f"{AMARILLO}¿Deseas actualizar la cantidad? (s/n):\n{BLANCO}# ").lower()
    if resp_cantidad == 's':
        try:
            nueva_cantidad = int(input(F"{VERDE}Introduce la nueva cantidad:\n{BLANCO}# "))
        except ValueError:
            print(f"{ROJO}Entrada inválida para la cantidad. No se actualizará.")
    
    # Llama a la función de servicio para actualizar
    srv.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

def ejecutar_eliminar_producto(inventario):
    """Solicita nombre y elimina un producto."""
    print(f"{AMARILLO}\n-> Eliminar Producto")
    nombre = input(f"{VERDE}Introduce el nombre del producto a eliminar:\n{BLANCO}# ")
    srv.eliminar_producto(inventario, nombre)


def ejecutar_mostrar_estadisticas(inventario):
    """Calcula y muestra las estadísticas del inventario."""
    print(f"{AMARILLO}\n-> Estadísticas del Inventario")
    stats = srv.calcular_estadisticas(inventario)
    if stats:
        print(f"{VERDE}  - Unidades totales: {stats['unidades_totales']}")
        print(f"  - Valor total del inventario: ${stats['valor_total']:.2f}")
        print(f"  - Producto más caro: {stats['producto_mas_caro']['nombre']} (${stats['producto_mas_caro']['precio']:.2f})")
        print(f"  - Producto con mayor stock: {stats['producto_mayor_stock']['nombre']} ({stats['producto_mayor_stock']['cantidad']} unidades)")
    else:
        print(f"{AMARILLO}El inventario está vacío, no se pueden calcular estadísticas.")

def ejecutar_guardar_inventario(inventario):
    """Solicita ruta y guarda el inventario."""
    print(f"{VERDE}\n-> Guardar Inventario")
    ruta = input(f"{VERDE}Introduce la ruta/nombre del archivo (ej. inventario.csv):\n{BLANCO}# ")
    arch.guardar_csv(inventario, ruta)

def ejecutar_cargar_inventario(inventario):
    """Gestiona la carga de inventario desde CSV."""
    print(f"{VERDE}\n-> Cargar Inventario")
    ruta = input(f"Introduce la ruta del archivo CSV a cargar:\n{BLANCO}# ")
    
    cargados, invalidos = arch.cargar_csv(ruta)
    
    if cargados is None:
        return # Error crítico al abrir/leer archivo

    print(f"{VERDE}\nProductos válidos detectados: {len(cargados)}")
    if invalidos > 0:
        print(f"{AMARILLO}Filas inválidas omitidas: {invalidos}")

    if not cargados:
        print(f"{AMARILLO}No se encontraron productos válidos para importar.")
        return

    while True:
        resp = input(f"{AMARILLO}¿Sobrescribir inventario actual? (S/N): ").lower()
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
    
    print(f"{VERDE}\nOperación completada: {accion}.")
    print(f"Estado actual: {len(inventario)} tipos de productos en inventario.{RESET}")