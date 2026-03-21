import csv
from funtions.extras import *


def guardar_csv(inventario, ruta, incluir_header=True):
    # Validar que el inventario no esté vacío
    if not inventario:
        print(f"{AMARILLO}El inventario está vacío, no hay datos para guardar.")
        return

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            if incluir_header:
                escritor.writerow(['nombre', 'precio', 'cantidad'])
            
            for nombre, datos in inventario.items():
                escritor.writerow([nombre, datos['precio'], datos['cantidad']])
        
        print(f"{VERDE}Inventario guardado en: {ruta}")

    except PermissionError:
        print(f"{ROJO}Error: Permiso denegado para escribir en '{ruta}'. Verifica que el archivo no esté abierto.")
    except IOError as e:
        print(f"{ROJO}Error al intentar guardar el archivo: {e}")

def cargar_csv(ruta):
    
    inventario_cargado = {}
    filas_invalidas = 0

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            
            try:
                encabezado = next(lector)
            except StopIteration:
                print(f"{AMARILLO}El archivo está vacío.")
                return None, 0

            # Validar encabezado
            encabezado = [h.strip().lower() for h in encabezado]
            if encabezado != ['nombre', 'precio', 'cantidad']:
                print(f"{ROJO}Error: El archivo debe tener encabezado: nombre,precio,cantidad")
                return None, 0

            for fila in lector:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                
                try:
                    nombre = fila[0].strip().title()
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if not nombre or precio < 0 or cantidad < 0:
                        raise ValueError
                    
                    inventario_cargado[nombre] = {'precio': precio, 'cantidad': cantidad}
                except ValueError:
                    filas_invalidas += 1

        return inventario_cargado, filas_invalidas

    except FileNotFoundError:
        print(f"{ROJO}Error: No se encontró el archivo '{ruta}'.")
        return None, 0
    except UnicodeDecodeError:
        print(f"{ROJO}Error: Codificación de archivo inválida (se espera UTF-8).")
        return None, 0
    except Exception as e:
        print(f"{ROJO}Error inesperado: {e}")
        return None, 0