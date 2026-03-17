from colores import *

inventario = []

inventario = []


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
    producto = input("\nIngrese el nombre del producto:\n# ")
    limpiar_pantalla()
    precio = float(input("\nIngrese el precio del producto:\n# "))
    limpiar_pantalla()
    cantidad = int(input("\nIngrese la cantidad del producto:\n# "))
            
    nuevo_producto = {"nombre": producto, "precio": precio, "cantidad": cantidad}
    inventario.append(nuevo_producto)
            
    print("Producto agregado con éxito")
    input("Presione enter para continuar")
    limpiar_pantalla()

def mostrar_inventario():
    limpiar_pantalla()
    print("\nInventario:\n")
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    input("\nPresione enter para continuar")
    limpiar_pantalla()

def salir():
    continuar = input("¿Está seguro de que desea salir? (si/no): ")
    limpiar_pantalla()