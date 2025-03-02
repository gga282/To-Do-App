import json
import questionary
import sys
from datetime import datetime
from view_task import view_task
import os

user_list={"Task":"","Deadline":"","Added Time":"","Category":"","Status":""}

def add_task():
    
    choice=questionary.select("Choose Category: ",choices=["Work","Personal","Urgent","Exit"]).ask()
    if choice=="Work":
        task_input("Work")
    elif choice=="Personal":
        task_input("Personal")
    elif choice=="Urgent":
        task_input("Urgent")
    else:
        sys.exit()

        
def task_input(ctgry):
    task_data=[]
    if os.path.exists("task.json"):
        with open("task.json","r") as f:
            try:
                task_data=json.load(f)
                if not isinstance(task_data,list):
                    task_data=[]
            except json.JSONDecodeError:
                task_data=[]

    while True:
        user_list={
            "Task":input("Please add your task explanation: "),
            "Deadline": datetime.strptime(input("Please add your deadline (YYYY-MM-DD): "), "%Y-%m-%d").strftime("%Y-%m-%d"),
            "Added Time":datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "Category":ctgry,
            "Status":"Pending"
        }
        task_data.append(user_list)
        ans=input("Enter Q to quit:")
        if ans.lower()=='q':
            break

    list_to_json(task_data)


def list_to_json(task_data):
    with open("task.json","w") as f:
        json.dump(task_data,f,indent=4)

def update_task():

    choice=questionary.select("Update Task Status: ",choices=["Pending","Done"]).ask()

    if choice=="Pending":
        user_list["Status"]="Pending"
    elif choice=="Done":
        user_list["Status"]="Done"

def remove_task():
    json_file_path=view_task()
    if json_file_path:
        os.remove(json_file_path)
        print(f"{json_file_path} has been removed.")

def check_task_deadline(data): #json file
    deadline_date=datetime.strptime(data["Deadline"],"%Y-%m-%d")
    today=datetime.today().date()
    if deadline_date<today:
        print(f"{data["Task"]} is due.")
        data["Status"]="Overdue!!!"
    else:
        print(f"You have {(deadline_date-today).days} days left to complete '{data['Task']}'.")

    




