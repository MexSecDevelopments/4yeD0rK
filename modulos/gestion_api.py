import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

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

def google_search_parallel(dorks, api_key, cse_id):
    """
    Ejecuta búsquedas en Google Custom Search en paralelo para una lista de dorks.

    Args:
        dorks (list): Lista de dorks (consultas de búsqueda) a ejecutar.
        api_key (str): Clave de la API de Google.
        cse_id (str): Identificador del Motor de Búsqueda Personalizado.

    Returns:
        list: Lista de resultados de las búsquedas.
    """
    def worker(dork):
        return google_search(dork, api_key, cse_id)
    
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_dork = {executor.submit(worker, dork): dork for dork in dorks}
        
        for future in as_completed(future_to_dork):
            dork = future_to_dork[future]
            try:
                data = future.result()
                results.append(data)  # O procesar los datos según sea necesario
            except Exception as exc:
                print(f'{dork} generó una excepción: {exc}')
    
    return results


