import questionary 
from add_task import add_task
from view_task import show_task
import os

def main_menu():
    print("Welcome to To Do App")
    print("Please choose one option:\n")
    choice=questionary.select("Menu",choices=["Add a Task","View Tasks","Mark a Task as Done","Remove Task From the List","Settings","Exit"]).ask()
    print("User selected:", choice)

    if choice=="Add a Task":
        add_task()
    elif choice=="View Tasks":
        print("Calling show_task()...")
        show_task()
    else:
        print("Error")
    #elif choice=="Mark a Task as Done":

    #elif choice=="Remove Task From the List":
    
    #elif choice=="Settings":
        

    #elif choice=="Show the list":


main_menu()