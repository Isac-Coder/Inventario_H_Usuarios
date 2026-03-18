from archivos import limpiar_pantalla

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario o actualiza la cantidad ya existente.

    Args:
        inventario (dict): Diccionario que representa el inventario.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad del producto.

    Returns:
        bool: True si el producto fue agregado/actualizado, False si los datos son inválidos.
    """
    # Validación de datos de entrada
    if not isinstance(nombre, str) or not nombre.strip():
        print("Error: El nombre del producto no puede estar vacío.")
        return False
    if not isinstance(precio, (int, float)) or precio < 0:
        print("Error: El precio no puede ser un número negativo.")
        return False
    if not isinstance(cantidad, int) or cantidad < 0:
        print("Error: La cantidad no puede ser un número negativo.")
        return False

    nombre = nombre.strip().title() # Estandarizar el nombre

    if nombre in inventario:
        # Si el producto existe, actualiza la cantidad
        inventario[nombre]['cantidad'] += cantidad
        print(f"Cantidad del producto '{nombre}' actualizada.")
        input("Pulsa Enter para continuar...")
        limpiar_pantalla()
    else:
        # Si es un producto nuevo, lo añade al inventario
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
        print(f"Producto '{nombre}' agregado al inventario.")
        input("Pulsa Enter para continuar...")
        limpiar_pantalla()
    
    return True

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en un formato claro.

    Args:
        inventario (dict): El inventario de productos.
    """
    print("\n--- Inventario Actual ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        # Imprime una tabla con los productos
        print(f"{'Producto':<20} | {'Precio':>10} | {'Cantidad':>10}")
        print("-" * 45)
        for nombre, datos in inventario.items():
            print(f"{nombre:<20} | ${datos['precio']:>9.2f} | {datos['cantidad']:>10}")
    print("-" * 45)

def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario por su nombre.

    Args:
        inventario (dict): El inventario de productos.
        nombre (str): El nombre del producto a buscar.

    Returns:
        dict: Un diccionario con los datos del producto si se encuentra, de lo contrario None.
    """
    nombre = nombre.strip().title()
    return inventario.get(nombre)

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente.

    Args:
        inventario (dict): El inventario de productos.
        nombre (str): El nombre del producto a actualizar.
        nuevo_precio (float, optional): El nuevo precio del producto.
        nueva_cantidad (int, optional): La nueva cantidad del producto.

    Returns:
        bool: True si el producto fue actualizado, False si no se encontró o los datos son inválidos.
    """
    nombre = nombre.strip().title()
    producto = inventario.get(nombre)

    if not producto:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return False

    # Actualiza el precio si se proporciona y es válido
    if nuevo_precio is not None:
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            print("Error: El nuevo precio no puede ser un número negativo.")
            return False
        producto['precio'] = nuevo_precio
        print(f"Precio de '{nombre}' actualizado a ${nuevo_precio:.2f}.")

    # Actualiza la cantidad si se proporciona y es válida
    if nueva_cantidad is not None:
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            print("Error: La nueva cantidad no puede ser un número negativo.")
            return False
        producto['cantidad'] = nueva_cantidad
        print(f"Cantidad de '{nombre}' actualizada a {nueva_cantidad}.")
        
    if nuevo_precio is None and nueva_cantidad is None:
        print("No se proporcionaron datos para actualizar.")
        return False

    return True

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Args:
        inventario (dict): El inventario de productos.
        nombre (str): El nombre del producto a eliminar.

    Returns:
        bool: True si el producto fue eliminado, False si no se encontró.
    """
    nombre = nombre.strip().title()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
        return True
    else:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return False

def calcular_estadisticas(inventario):
    """
    Calcula estadísticas sobre el inventario.

    Calcula:
    - Unidades totales (suma de cantidad).
    - Valor total (suma de precio * cantidad).
    - Producto más caro.
    - Producto con mayor stock.

    Args:
        inventario (dict): El inventario de productos.

    Returns:
        dict: Un diccionario con las estadísticas calculadas. Retorna None si el inventario está vacío.
    """
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
