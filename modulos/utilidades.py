# utilidades

import os

def limpiar_consola():
    """Limpia la consola, tanto en Windows como en Unix/Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_entrada(mensaje, tipo=str, rango=None):
    """
    Solicita al usuario una entrada, asegurándose de que sea del tipo y rango especificados.

    Args:
        mensaje (str): Mensaje a mostrar al solicitar la entrada.
        tipo (type): Tipo de dato esperado (por defecto, str).
        rango (tuple, optional): Un rango de valores válidos para entradas numéricas.

    Returns:
        Entrada validada del usuario, convertida al tipo especificado.
    """
    while True:
        entrada_usuario = input(mensaje)
        try:
            entrada_usuario = tipo(entrada_usuario)
            if rango and entrada_usuario not in range(rango[0], rango[1] + 1):
                raise ValueError
            return entrada_usuario
        except ValueError:
            print(f"Entrada inválida. Por favor, introduce un valor {'entre ' + str(rango[0]) + ' y ' + str(rango[1]) if rango else 'válido'}.")

