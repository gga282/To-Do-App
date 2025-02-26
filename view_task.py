import glob
import questionary
import json
from rich import table
from rich.console import Console
import os

def view_task():
    
    files_path=glob.glob("*.json")

    if not files_path:
        print("No Task file found")
        return None

    choice=questionary.select("Select file",choices=files_path).ask()

    if choice=="Exit" or choice is None:
        return None
    
    return choice

def show_task():
    json_file=view_task()

    if json_file==None:
        print("Nothing to show")
        return 
    
    with open(json_file,"r") as f:
        data=json.load(f)
    


    task_table = table.Table(title="To-Do-List")
    task_table.add_column("Tasks",justify="center", style="cyan", no_wrap=True)
    task_table.add_column("Deadline",justify="center",style="magenta")
    task_table.add_column("Added Time",justify="center",style="red")
    task_table.add_column("Category",justify="center")
    task_table.add_column("Status",justify="center")
    for i,j in enumerate(data):
        task_table.add_row(j["Task"], j["Deadline"], j["Added Time"], j["Category"],j["Status"])
    

    console = Console()
    console.print(task_table)