import glob
import questionary
import json
from rich import table
from rich.console import Console
import os
from datetime import datetime
import re
def view_task():
    files_path = glob.glob("*.json")

    if not files_path:
        print("No Task file found")
        return None
    
    try:
        choice = questionary.select("Select file", choices=files_path + ["Exit"]).ask()
    except Exception as e:
        print(f"ERROR: questionary.select() failed with exception: {e}")
        return None
    
    if choice == "Exit":
        print("Returning to main menu")
        return None
    
    return choice

def show_task():
    json_file = view_task()

    if json_file is None:
        print("Nothing to show")
        return 
    
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
        
        task_table = table.Table(title="To-Do-List")
        task_table.add_column("Tasks", justify="center", style="cyan", no_wrap=True)
        task_table.add_column("Deadline", justify="center", style="magenta")
        task_table.add_column("Added Time", justify="center", style="red")
        task_table.add_column("Category", justify="center")
        task_table.add_column("Status", justify="center")
        
        for i, j in enumerate(data):
            if j["Status"] == "Overdue!!!":
                task_table.add_row(j["Task"], j["Deadline"], j["Added Time"], j["Category"], f"[red]{j['Status']}[/red]")
            else:
                task_table.add_row(j["Task"], j["Deadline"], j["Added Time"], j["Category"], j["Status"])
        
        console = Console()
        console.print(task_table)
        
    
        input("\nPress Enter to continue...")
        
    except Exception as e:
        print(f"Error displaying tasks: {e}")
        input("\nPress Enter to continue...")


def search_menu():
    json_file = view_task()
    if json_file is None:
        print("No file selected for search")
        input("\nPress Enter to continue...")
        return
    choice = questionary.select("Please search area", choices=["Task Name", "Deadline", "Category", "Status"]).ask()
    filter_key=get_filter_key(choice)
    if filter_key:
        filter_task(choice,filter_key,json_file)


def get_filter_key(choice):
    if choice=="Task Name":
        return questionary.text("Enter search term or regex pattern: ").ask()
    elif choice=="Deadline":
        return questionary.select("Please search area", choices=["Pending", "Done"]).ask()
    elif choice=="Category":
        return questionary.select("Choose Category", choices=["Work", "Personal", "Urgent"]).ask()
    elif choice=="Status":
        return questionary.select("Please search area", choices=["Pending", "Done"]).ask()
    else:
        return 


def filter_task(choice, filter_key, json_file):
    search = []
    try:
        with open(json_file, "r") as f:
            data = json.load(f)

        for task in data:
            if choice == "Task Name" and re.search(filter_key, task["Task"], re.IGNORECASE):
                search.append(task)
            elif choice == "Category" and re.search(filter_key, task["Category"], re.IGNORECASE):
                search.append(task)
            elif choice == "Status" and re.search(filter_key, task["Status"], re.IGNORECASE):
                search.append(task)
        
        console = Console()
        task_table = table.Table(title="To-Do-List")
        task_table.add_column("Tasks", justify="center", style="cyan", no_wrap=True)
        task_table.add_column("Deadline", justify="center", style="magenta")
        task_table.add_column("Added Time", justify="center", style="red")
        task_table.add_column("Category", justify="center")
        task_table.add_column("Status", justify="center")
        
        if search:
            for task in search:
                task_table.add_row(task["Task"], task["Deadline"], task["Added Time"], task["Category"], task["Status"])
            console.print(task_table)
        else:
            console.print("[bold red]No results found.[/bold red]")
    
    except Exception as e:
        print(f"Error displaying tasks: {e}")
    
    # Add pause to see results
    input("\nPress Enter to continue...")



