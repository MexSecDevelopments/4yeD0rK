# seleccion_categoria

def select_category(available_categories):
    """
    Solicita al usuario que seleccione una categoría de dorks de una lista proporcionada.
    
    Args:
        available_categories (list): Una lista de categorías disponibles para elegir.
    
    Returns:
        str: La categoría seleccionada por el usuario.
    """
    print("Selecciona la categoría de Dorks que utilizarás contra el dominio:")
    for i, category in enumerate(available_categories, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("Ingresa el número de la categoría: ")) - 1
            if 0 <= choice < len(available_categories):
                return available_categories[choice]
            else:
                print("Por favor, selecciona un número válido de la lista.")
        except ValueError:
            print("Por favor, introduce un número.")
