# Este codigo tiene algunas mejoras como:
# Una interfaz grafica mejorada usando rich
# para agregar colores, tablas estilizadas y una interfaz más visual y atractiva.
# Se agregó una lista (historial_ejecuciones) para almacenar los scripts ejecutados.
# Edición de Scripts Directamente desde el Menú.

import os
import subprocess

# Manejo de importación de rich
try:
    from rich.console import Console
    from rich.table import Table
    from rich.prompt import Prompt

    console = Console()
except ModuleNotFoundError:
    print("El módulo 'rich' no está instalado. Instálalo con 'pip install rich'.")
    exit()

# Lista para almacenar historial de scripts ejecutados
historial_ejecuciones = []


def mostrar_codigo(ruta_script):
    """Muestra el código de un script seleccionado."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            console.print(f"\n[bold green]--- Código de {ruta_script} ---[/bold green]\n")
            console.print(codigo, style="cyan")
            return codigo
    except FileNotFoundError:
        console.print("[bold red]El archivo no se encontró.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error al leer el archivo:[/bold red] {e}")


def ejecutar_codigo(ruta_script):
    """Ejecuta un script de Python en una nueva terminal."""
    try:
        console.print(f"[bold blue]Ejecutando:[/bold blue] {ruta_script}")
        historial_ejecuciones.append(ruta_script)
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        console.print(f"[bold red]Error al ejecutar el código:[/bold red] {e}")


def editar_script(ruta_script):
    """Permite editar un script directamente desde el menú."""
    console.print(f"[bold yellow]Editando el script:[/bold yellow] {ruta_script}")
    if os.name == 'nt':
        os.system(f'notepad {ruta_script}')
    else:
        os.system(f'nano {ruta_script}')


def mostrar_menu():
    """Muestra el menú principal con una tabla de opciones mejorada."""
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2', '3': 'Ver Historial'}

    while True:
        console.clear()
        table = Table(title="Dashboard - Gestión de Proyectos", style="bold magenta")
        table.add_column("Opción", justify="center", style="cyan", no_wrap=True)
        table.add_column("Descripción", style="green")

        for key, value in unidades.items():
            table.add_row(key, value)
        table.add_row("0", "Salir")

        console.print(table)
        eleccion = Prompt.ask("Seleccione una opción")

        if eleccion == '0':
            console.print("[bold red]Saliendo del programa...[/bold red]")
            break
        elif eleccion == '3':
            ver_historial()
        elif eleccion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion]))
        else:
            console.print("[bold red]Opción no válida. Intenta de nuevo.[/bold red]")


def ver_historial():
    """Muestra el historial de scripts ejecutados."""
    console.print("[bold cyan]Historial de Ejecuciones:[/bold cyan]")
    for i, script in enumerate(historial_ejecuciones, 1):
        console.print(f"{i}. {script}", style="yellow")
    input("Presiona Enter para volver al menú principal...")


def mostrar_sub_menu(ruta_unidad):
    """Muestra un submenú con las carpetas disponibles en la unidad."""
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        console.clear()
        console.print(f"[bold magenta]Submenú - {ruta_unidad}[/bold magenta]")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            console.print(f"{i} - {carpeta}", style="cyan")
        console.print("0 - Regresar")

        eleccion = Prompt.ask("Seleccione una carpeta")

        if eleccion == '0':
            break
        else:
            try:
                index = int(eleccion) - 1
                if 0 <= index < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[index]))
                else:
                    console.print("[bold red]Opción no válida.[/bold red]")
            except ValueError:
                console.print("[bold red]Entrada inválida.[/bold red]")


def mostrar_scripts(ruta_sub_carpeta):
    """Lista y permite ejecutar o editar scripts dentro de una carpeta."""
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        console.clear()
        console.print(f"[bold magenta]Scripts en {ruta_sub_carpeta}[/bold magenta]")
        for i, script in enumerate(scripts, start=1):
            console.print(f"{i} - {script}", style="cyan")
        console.print("0 - Regresar")

        eleccion = Prompt.ask("Seleccione un script")

        if eleccion == '0':
            break
        else:
            try:
                index = int(eleccion) - 1
                if 0 <= index < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[index])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        console.print("1 - Ejecutar | 2 - Editar | 0 - Regresar", style="yellow")
                        accion = Prompt.ask("Seleccione una acción")
                        if accion == '1':
                            ejecutar_codigo(ruta_script)
                        elif accion == '2':
                            editar_script(ruta_script)
                else:
                    console.print("[bold red]Opción no válida.[/bold red]")
            except ValueError:
                console.print("[bold red]Entrada inválida.[/bold red]")


if __name__ == "__main__":
    mostrar_menu()
