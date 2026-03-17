from funciones import *
from colores import *

limpiar_pantalla()

def registrar_operacion(productos):
    """
    Agrega una descripción de operación al historial.
    """
    productos.append(productos)

continuar = "no"
inventario = {}
i = 0

while continuar == "no":
    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            limpiar_pantalla()
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            registrar_operacion(f"el producto {(nombre)}. con precio de: $ {precio} y cantidad de: {cantidad}")
            print("Producto agregado con éxito")
            input("Presione enter para continuar")
            limpiar_pantalla()

        elif opcion == 2:
            
            if not inventario:
                print("No hay productos en el inventario")
            else:
                print("Inventario:")
                for i, productos in enumerate(inventario):
                    print(f"{i}. {productos}")
            input("Presione enter para continuar")
            limpiar_pantalla()


        elif opcion == 3:
            print()

        elif opcion == 4:
            continuar = input("(si/no): ")
            limpiar_pantalla()

        else:
            print("Opción inválida")
    except ValueError:
        print("Opción inválida")