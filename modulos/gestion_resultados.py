# gestion_resultados

from rich.console import Console
from rich.table import Table

# Inicializa un objeto de consola para salida enriquecida
console = Console()

def show_results_with_style(results, query):
    """Muestra los resultados de la búsqueda en una tabla formateada."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Título", style="dim", width=50)
    table.add_column("Link")

    if "items" in results:
        for item in results['items']:
            table.add_row(item['title'], item['link'])
        console.print(f"\n[green]Resultados para: {query}[/green]")
        console.print(table)
    else:
        console.print(f"\n[red]No se encontraron resultados para: {query}[/red]")
