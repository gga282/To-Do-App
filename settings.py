from ics import Calendar, Event
import questionary
import glob
from view_task import view_task
from datetime import datetime
import json
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def menu_settings():
    
    choice=questionary.select("Please select ",choices=["Export to Calendar","Export to CSV","Export to PDF"]).ask()
    if choice=="Export to Calendar":
        export_to_calendar()
    if choice=="Export to CSV":
        export_to_csv()
    if choice=="Export to PDF":
        export_to_pdf()

def export_to_calendar():
    
    json_file_path=view_task()
    c=Calendar()
    e=Event()
    with open(json_file_path,'r') as f:
        json_file = json.load(f)
    for i,j in enumerate(json_file):
        e.name=j["Task"]
        e.begin=datetime.strptime(j["Added Time"], "%d-%m-%Y %H:%M:%S").strftime("%Y%m%dT%H%M%SZ")
        e.end=datetime.strptime(j["Deadline"], "%Y-%m-%d")
        e.description = j["Task"]
        c.events.add(e)

        with open(f'my_task_{i}.ics','w') as my_file:
            my_file.writelines(c.serialize())

def export_to_csv(): #i should improve this with pandas
    json_file_path=view_task()
    with open(json_file_path,"r") as f:
        json_file=json.load(f)
    
    for i,j in enumerate(json_file):
        with open(f'my_task_{i}.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Task,Deadline,Added Time,Category,Status"])
            writer.writerow([j['Task'],j['Deadline'],j['Added Time'],j['Category'],j['Status']])


    
def export_to_pdf():
    file_name=input("Please enter filename: ")

    json_file_path=view_task()
    with open(json_file_path,"r") as f:
        json_file=json.load(f)
    c=canvas.Canvas(file_name+'.pdf',pagesize=letter)
    c.setFont("Helvetica",12)
    y=750

    for task in json_file:
        c.drawString(100,y,f"Task: {task['Task']}")
        c.drawString(100,y-20,f"Deadline: {task['Deadline']}")
        c.drawString(100,y-40,f"Added Time: {task['Added Time']}")
        c.drawString(100, y - 60, f"Category: {task['Category']}")
        c.drawString(100, y - 80, f"Status: {task['Status']}")
        y-=120

    c.save()



