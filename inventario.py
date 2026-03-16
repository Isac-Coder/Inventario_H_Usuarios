from limpiar_pantalla import limpiar_pantalla
limpiar_pantalla()


# Solicitar el nombre del producto
while True:
    nombre = input("Ingrese el nombre del producto:\n# ")

    if nombre.replace(" ", "").isalpha():
        break
    else:
        print("Error: el nombre solo debe contener letras.")
        input("Presione Enter para continuar...")
        limpiar_pantalla()


# Solicitar el precio del producto
while True:
    try:
        precio = float(input("Ingrese el precio del producto:\n# "))
        break
    except:
        print("Error: debe ingresar un número válido.")
        input("Presione Enter para continuar...")
        limpiar_pantalla()

# Solicitar la cantidad del producto
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto:\n# "))
        break
    except:
        print("Error: debe ingresar un número entero válido.")
        input("Presione Enter para continuar...")
        limpiar_pantalla()

# Calcular el costo total
costo_total = precio * cantidad

# Mostrar los resultados
print("\n----- RESUMEN DEL PRODUCTO -----")
print(f"Producto: {nombre} | Precio: {int(precio)} | Cantidad: {cantidad} | Total: {costo_total}")