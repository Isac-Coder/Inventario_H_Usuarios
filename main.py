from funciones import *
from colores import *

limpiar_pantalla()


continuar = "no"
inventario = []

while continuar == "no":
    try:
        menu()
        opcion = int(input("\nIngrese una opción:\n# "))

        if opcion == 1:
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

        elif opcion == 2:
            limpiar_pantalla()
            print("\nInventario:\n")
            for i, producto in enumerate(inventario, 1):
                print(f"{i}. Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
            input("\nPresione enter para continuar")
            limpiar_pantalla()


        elif opcion == 3:
            print()

        elif opcion == 4:
            continuar = input("¿Está seguro de que desea salir? (si/no): ")
            limpiar_pantalla()

        else:
            print("Opción inválida")
    except ValueError:
        print("Opción inválida")
        input("Presione enter para continuar")
        limpiar_pantalla()