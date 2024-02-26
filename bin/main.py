from rich.console import Console
from rich.markdown import Markdown
from modulos.generador_dorks import generate_dorks_for_category
from modulos.gestion_resultados import show_results_with_style
from modulos.seleccion_categoria import select_category
from modulos.utilidades import limpiar_consola, validar_entrada
from modulos.gestion_api import google_search  # Asegúrate de haber implementado esta función correctamente

# Creando un objeto de consola para una salida rica
console = Console()

# Configuración inicial
API_KEY = "tu_clave_de_api"  # Reemplaza con tu clave de API
CSE_ID = "tu_id_de_motor_de_búsqueda_personalizado"  # Reemplaza con tu ID de motor de búsqueda personalizado

if __name__ == "__main__":
    try:
        limpiar_consola()  # Limpia la consola al inicio del programa
        console.print(Markdown("# Bienvenido a **4yeD0rK**\n## An _ExorciseThat_ Project"), style="bold cyan")
        start_choice = validar_entrada("[bold magenta]Comenzar (yes/y) o Abortar (no/n): [/bold magenta]", tipo=str)

        if start_choice.lower() in ['yes', 'y']:
            DOMAIN = input("Por favor, introduce el dominio a escanear (ejemplo: ejemplo.com): ").strip()

        while start_choice.lower() in ['yes', 'y']:
            selected_category = select_category()  # Asume que select_category maneja internamente las categorías
            limpiar_consola()  # Limpia la consola antes de mostrar nuevos datos

            mode_choice = validar_entrada("Selecciona el modo (0: Light, 1: Normal, 2: Diablo): ", tipo=int, rango=(0, 2))
            mode = ["Light", "Normal", "Diablo"][mode_choice]

            selected_dorks = generate_dorks_for_category(selected_category, DOMAIN, mode)
            for dork in selected_dorks:
                console.print(f"[bold cyan]Buscando:[/bold cyan] [italic]{dork}[/italic]")
                results = google_search(dork, API_KEY, CSE_ID)  # Ajustado para pasar las claves como argumentos
                show_results_with_style(results, dork)

            console.print("[green]Escaneo finalizado.[/green]")
            console.print("[yellow]Si no obtuviste resultados, considera incrementar el nivel de escaneo para una búsqueda más exhaustiva.[/yellow]")

            opcion = validar_entrada("Elige una opción:\n1) Probar con otra categoría\n2) Incrementar a nivel DIABLO\nSelecciona una opción: ", tipo=int, rango=(1, 2))

            if opcion == 2:
                mode = "Diablo"
                selected_dorks = generate_dorks_for_category(selected_category, DOMAIN, mode)
                for dork in selected_dorks:
                    console.print(f"[bold cyan]Buscando:[/bold cyan] [italic]{dork}[/italic]")
                    results = google_search(dork, API_KEY, CSE_ID)
                    show_results_with_style(results, dork)
                continue  # Asegura que el bucle continúe si se elige incrementar el nivel

            break  # Salir del bucle si la opción no es continuar

    except KeyboardInterrupt:
        console.print("\n[bold red]Escaneo interrumpido, abortando...[/bold red]")



