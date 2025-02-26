import questionary 
from add_task import add_task,update_task,remove_task
from view_task import show_task
from settings import menu_settings
import os,sys

def main_menu():
    print("Welcome to To Do App")
    print("Please choose one option:\n")
    choice=questionary.select("Menu",choices=["Add a Task","View Tasks","Mark a Task as Done","Remove Task From the List","Settings","Exit"]).ask()
    print("User selected:", choice)

    if choice=="Add a Task":
        add_task()
    elif choice=="View Tasks":
        show_task()
    elif choice=="Mark a Task as Done":
        update_task()
    elif choice=="Remove Task From the List":
        remove_task()
    elif choice=="Settings":
        menu_settings()
    elif choice=="Exit":
        sys.exit(1)   
        
        

    #elif choice=="Show the list":


main_menu()