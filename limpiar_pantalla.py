def limpiar_pantalla():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')