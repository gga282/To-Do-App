import json
import questionary
import sys
from datetime import datetime

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
    user_list={"Task":"","Deadline":"","Added Time":"","Category":""}

    for i in user_list.keys():
        if i=="Task":
            user_list[i]=input("Please add your task explanition: ")
        elif i=="Deadline":
            user_list[i]=input("Please add your deadline: ")
        elif i=="Added Time":
            user_list[i]=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        elif i=="Category":
            user_list[i]=ctgry
    
    list_to_json(user_list)


def list_to_json(user_list):
    json_object=json.dumps(user_list,indent=4)
    with open("task.json","w") as f:
        json.dump(user_list, f, indent=4)




