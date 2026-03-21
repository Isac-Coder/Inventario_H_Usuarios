from funtions.extras import *


def agregar_producto(inventario, nombre, precio, cantidad):
    
    # Validación de datos de entrada
    if not isinstance(nombre, str) or not nombre.strip():
        print(f"{ROJO}Error: El nombre del producto no puede estar vacío.")
        return False
    if not isinstance(precio, (int, float)) or precio < 0:
        print(f"{ROJO}Error: El precio no puede ser un número negativo.")
        return False
    if not isinstance(cantidad, int) or cantidad < 0:
        print(f"{ROJO}Error: La cantidad no puede ser un número negativo.")
        return False

    nombre = nombre.strip().title() # Estandarizar el nombre

    if nombre in inventario:
        # Si el producto existe, actualiza la cantidad
        inventario[nombre]['cantidad'] += cantidad
        print(f"{VERDE}Cantidad del producto '{nombre}' actualizada.")
    else:
        # Si es un producto nuevo, lo añade al inventario
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
        print(f"{VERDE}Producto '{nombre}' agregado al inventario.")
    
    return True

def mostrar_inventario(inventario):
    
    print(f"{AMARILLO}\n--- Inventario Actual ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        # Imprime una tabla con los productos
        print(f"{BLANCO}{'Producto':<20} | {'Precio':>10} | {'Cantidad':>10}")
        print("-" * 45)
        for nombre, datos in inventario.items():
            print(f"{nombre:<20} | ${datos['precio']:>9.2f} | {datos['cantidad']:>10}")
    print("-" * 45)

def buscar_producto(inventario, nombre):
    
    nombre = nombre.strip().title()
    return inventario.get(nombre)

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    
    nombre = nombre.strip().title()
    producto = inventario.get(nombre)

    if not producto:
        print(f"{ROJO}Error: El producto '{nombre}' no se encuentra en el inventario.")
        return False

    # Actualiza el precio si se proporciona y es válido
    if nuevo_precio is not None:
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            print("Error: El nuevo precio no puede ser un número negativo.")
            return False
        producto['precio'] = nuevo_precio
        print(f"{BLANCO}Precio de '{nombre}' actualizado a ${nuevo_precio:.2f}.")

    # Actualiza la cantidad si se proporciona y es válida
    if nueva_cantidad is not None:
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            print(f"{ROJO}Error: La nueva cantidad no puede ser un número negativo.")
            return False
        producto['cantidad'] = nueva_cantidad
        print(f"{BLANCO}Cantidad de '{nombre}' actualizada a {nueva_cantidad}.")
        
    if nuevo_precio is None and nueva_cantidad is None:
        print(f"{AMARILLO}No se proporcionaron datos para actualizar.")
        return False

    return True

def eliminar_producto(inventario, nombre):
    
    nombre = nombre.strip().title()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
        return True
    else:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return False

def calcular_estadisticas(inventario):
    
    if not inventario:
        return None

    # Lambda para calcular el subtotal de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    # Cálculo de métricas solicitadas
    unidades_totales = sum(datos['cantidad'] for datos in inventario.values())
    valor_total = sum(subtotal(datos) for datos in inventario.values())

    # Encontrar productos destacados
    prod_mas_caro = max(inventario.items(), key=lambda item: item[1]['precio'])
    prod_mayor_stock = max(inventario.items(), key=lambda item: item[1]['cantidad'])

    # Empaquetado de los resultados
    estadisticas = {
        'unidades_totales': unidades_totales,
        'valor_total': valor_total,
        'producto_mas_caro': {'nombre': prod_mas_caro[0], 'precio': prod_mas_caro[1]['precio']},
        'producto_mayor_stock': {'nombre': prod_mayor_stock[0], 'cantidad': prod_mayor_stock[1]['cantidad']}
    }

    return estadisticas
