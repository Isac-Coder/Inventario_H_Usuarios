from funciones import *
from colores import *

continuar = "no"
limpiar_pantalla()




while continuar == "no":
    try:
        menu()
        opcion = int(input("\nIngrese una opción:\n# "))

        if opcion == 1:
            pedir_producto()
            
        elif opcion == 2:
            mostrar_inventario()

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