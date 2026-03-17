from colores import *
inventario = []

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()

def menu():
    print(f"{BLANCO}BIENVENIDO AL INVENTARIO{BLANCO}\n")
    print(f"1.{VERDE} Agregar producto{BLANCO}")
    print(f"2. {VERDE}Mostrar inventario{BLANCO}")
    print(f"3. {VERDE}Calcular estadisticas{BLANCO}")
    print(f"4. {ROJO}Salir{BLANCO}")
    

def registrar_inventario(descripcion):
    """
    Agrega una descripción de operación al historial.
    """
    inventario.append(descripcion)

def inventario():
    print(f"{VERDE}╔══════════╗")
    print(f"║{BLANCO}INVENTARIO{VERDE}║")
    print(f"╚══════════╝{VERDE}\n")
    