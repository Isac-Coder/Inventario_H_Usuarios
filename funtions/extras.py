import os
import time, random

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargando():
    print(f"{VERDE}Cargando", end="")
    for _ in range(3):
        time.sleep(random.uniform(0.1, 0.4))
        print(".", end="", flush=True)


ROJO = "\u001b[31m"
VERDE = "\u001b[32m"
AMARILLO = "\u001b[33m"
BLANCO = "\u001b[37m"
RESET = "\u001b[0m"