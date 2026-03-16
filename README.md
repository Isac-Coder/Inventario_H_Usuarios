# 📦 Programa de Inventario de Productos

Este programa en **Python** permite registrar un producto en un inventario solicitando información al usuario desde la consola.  
El sistema valida los datos ingresados y calcula el **costo total del producto según su precio y cantidad**.

---

## 🚀 Funcionalidad

El programa realiza las siguientes acciones:

1. Solicita el **nombre del producto**.
2. Valida que el nombre solo contenga **letras y espacios**.
3. Solicita el **precio del producto**.
4. Verifica que el precio sea un **número válido**.
5. Solicita la **cantidad disponible**.
6. Valida que la cantidad sea un **número entero**.
7. Calcula el **costo total** multiplicando el precio por la cantidad.
8. Muestra un **resumen del producto registrado**.

---

## 🧮 Fórmula utilizada
```
costo_total = precio × cantidad
```


---

## 💻 Ejemplo de uso

```
Ingrese el nombre del producto: Manzanas
Ingrese el precio del producto: 2.5
Ingrese la cantidad del producto: 10

----- RESUMEN DEL PRODUCTO -----
Producto: Manzanas | Precio: 2.5 | Cantidad: 10 | Total: 25.0
```


---

## ⚠️ Validaciones implementadas

El programa incluye validaciones para evitar errores de entrada:

- El **nombre** solo puede contener letras.
- El **precio** debe ser un número (float).
- La **cantidad** debe ser un número entero.

Si el usuario ingresa un dato incorrecto, el programa mostrará un **mensaje de error y volverá a pedir el dato**.

---

## 🛠 Tecnologías utilizadas

- **Python 3**
- Entrada de datos con `input()`
- Validación con `try/except`
- Uso de ciclos `while`

---

## Diagrama de flujo
![alt text](image-1.png)