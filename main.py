from funtions.app import *
from funtions.servicios import *
from funtions.archivos import *
from funtions.extras import *


 # El inventario se define como un diccionario vacío al inicio.
inventario = {}
    
    # Bucle principal de la aplicación
while True:
        limpiar_pantalla()
        opcion = mostrar_menu()

        if opcion == '1':
            limpiar_pantalla()
            cargando()
            ejecutar_agregar_producto(inventario)
        elif opcion == '2':
            limpiar_pantalla()
            cargando()
            srv.mostrar_inventario(inventario)
        elif opcion == '3':
            limpiar_pantalla()
            cargando()
            ejecutar_buscar_producto(inventario)
        elif opcion == '4':
            limpiar_pantalla()
            cargando()
            ejecutar_actualizar_producto(inventario)
        elif opcion == '5':
            limpiar_pantalla()
            cargando()
            ejecutar_eliminar_producto(inventario)
        elif opcion == '6':
            limpiar_pantalla()
            cargando()
            ejecutar_mostrar_estadisticas(inventario)
        elif opcion == '7':
            limpiar_pantalla()
            cargando()
            ejecutar_guardar_inventario(inventario)
        elif opcion == '8':
            limpiar_pantalla()
            cargando()
            ejecutar_cargar_inventario(inventario)
        elif opcion == '9':
            print("\nGracias por usar el sistema. ¡Adiós!")
            break
        else:
            limpiar_pantalla()
            cargando()
            print("\nOpción no válida. Por favor, elige una opción del 1 al 9.")
        
        # Pausa para que el usuario pueda leer la salida antes de mostrar el menú de nuevo
        input("\nPulsa Enter para continuar...")