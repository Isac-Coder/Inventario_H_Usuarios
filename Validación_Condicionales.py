import servicios as srv
import app

def main():
    """Bucle principal de la aplicación."""
    inventario = {}
    ejecutando = True
    
    while ejecutando:
        try:
            app.mostrar_menu()
            opcion = input("Selecciona una opción (1-9): ").strip()

            if opcion == '1':
                app.ejecutar_agregar_producto(inventario)
            elif opcion == '2':
                srv.mostrar_inventario(inventario)
            elif opcion == '3':
                app.ejecutar_buscar_producto(inventario)
            elif opcion == '4':
                app.ejecutar_actualizar_producto(inventario)
            elif opcion == '5':
                app.ejecutar_eliminar_producto(inventario)
            elif opcion == '6':
                app.ejecutar_mostrar_estadisticas(inventario)
            elif opcion == '7':
                app.ejecutar_guardar_inventario(inventario)
            elif opcion == '8':
                app.ejecutar_cargar_inventario(inventario)
            elif opcion == '9':
                print("\n¡Gracias por usar el sistema! Saliendo...")
                ejecutando = False
            else:
                print("\nOpción no válida. Por favor, elige una opción del 1 al 9.")
            
            if ejecutando:
                input("\nPulsa Enter para continuar...")
        
        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Usa la opción 9 para salir.")
        except Exception as e:
            print(f"\nOcurrió un error inesperado en el menú: {e}")

if __name__ == "__main__":
    main()