from colores import *
import time
import random

inventario = []

def cargando():
    print(f"{BLANCO}Cargando", end="")
    for _ in range(3):
        time.sleep(random.uniform(0.1, 0.4))
        print(".", end="", flush=True)
    
def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(f"{BLANCO}BIENVENIDO AL INVENTARIO{BLANCO}\n")
    print(f"1.{VERDE} Agregar producto{BLANCO}")
    print(f"2. {VERDE}Mostrar inventario{BLANCO}")
    print(f"3. {VERDE}Calcular estadisticas{BLANCO}")
    print(f"4. {ROJO}Salir{BLANCO}")
    
def pedir_producto():
    
    limpiar_pantalla()
    cargando()
    limpiar_pantalla()
    
    producto = str(input(f"\n{BLANCO}Ingrese el nombre del producto:\n# "))
    
    limpiar_pantalla()
    cargando()
    limpiar_pantalla()
    
    precio = float(input("\nIngrese el precio del producto:\n# "))
    
    limpiar_pantalla()
    cargando()
    limpiar_pantalla()
    
    cantidad = int(input("\nIngrese la cantidad del producto:\n# "))
    nuevo_producto = {"nombre": producto, "precio": precio, "cantidad": cantidad}
    inventario.append(nuevo_producto)
            
    cargando()
    print("\nProducto agregado con éxito")
    input("Presione enter para continuar. ")

    limpiar_pantalla()

def mostrar_inventario():
    
    limpiar_pantalla()
    cargando()
    limpiar_pantalla()
    
    print("\nInventario:\n")
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    input("\nPresione enter para continuar. ")
    limpiar_pantalla()
    
def calcular_estadisticas():
    
    limpiar_pantalla()
    cargando()
    limpiar_pantalla()
    
    if not inventario:
        print("El inventario está vacío. No hay estadísticas para calcular.")
        input("\nPresione enter para continuar. ")
        limpiar_pantalla()
        return
        
    valor_total_inventario = sum(item['precio'] * item['cantidad'] for item in inventario)
    cantidad_total_productos = sum(item['cantidad'] for item in inventario)
    
    print(f"{BLANCO}--- Estadísticas del Inventario ---{BLANCO}\n")
    print(f"Valor total del inventario: ${valor_total_inventario:,.2f}")
    print(f"Cantidad total de productos registrados: {cantidad_total_productos}")
    input("\nPresione enter para continuar. ")
    limpiar_pantalla()