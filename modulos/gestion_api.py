import requests

def google_search(query, api_key, cse_id):
    """
    Realiza una búsqueda utilizando la API de Google Custom Search.

    Args:
        query (str): La consulta de búsqueda.
        api_key (str): Clave de la API de Google.
        cse_id (str): Identificador del Motor de Búsqueda Personalizado.

    Returns:
        dict: El resultado de la búsqueda en formato JSON.
    """
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
    }
    response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
    return response.json()

