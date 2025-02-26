from ics import Calendar, Event
import questionary
import glob
from view_task import view_task
from datetime import datetime
import json


def menu_settings():
    
    choice=questionary.select("Please select ",choices=["Export to Calendar"]).ask()
    if choice=="Export to Calendar":
        export_to_calendar()

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
    
    


