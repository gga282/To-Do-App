import questionary 
from add_task import add_task,update_task,remove_task
from view_task import show_task,search_menu
from settings import menu_settings
import os,sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich import print
from rich.box import ROUNDED

console=Console()

def main_menu():
    console.clear()
    console.print(Panel("[bold cyan]Welcome to To-Do App![/bold cyan]\n[green]Manage your tasks efficiently.[/green]",
                            title="[bold magenta]To-Do Manager[/bold magenta]",
                            border_style="blue",
                            box=ROUNDED))


    options={"1":"Add a Task","2":"View Tasks","3":"Mark a task as Done","4":"Remove Task From the List","5":"Settings","6":"Search","7":"Exit"}
    for key, value in options.items():
        console.print(f"[bold yellow]{key}[/bold  yellow]: [cyan]{value}[/cyan]")

    choice=Prompt.ask("[bold magenta]Select an option[/bold magenta]",choices=list(options.keys()))

    if choice=="1":
        add_task()
    elif choice=="2":
        show_task()
    elif choice=="3":
        update_task()
    elif choice=="4":
        remove_task()
    elif choice=="5":
        menu_settings()
    elif choice=="6":
        search_menu()
    elif choice=="7":
        console.print("[bold red]Exiting...[/bold red]")
        sys.exit(1)

    main_menu()


        
main_menu()