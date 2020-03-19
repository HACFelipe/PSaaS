from typing import List
from datetime import date

from entity.project_task import ProjectTask

class Project(object):
    """Model of Project"""

    def __init__(self, name : str, description : str):
        self.id = ""
        self.name = name
        self.description = description
        self.project_tasks : List[ProjectTask] = []


    def add_task(self, task : ProjectTask):
        task.id = self.generate_id()
        self.project_tasks.append(task)


    def generate_id(self) -> str:
        prefix = self.id + "PT"
        count = 0
        for task in self.project_tasks:
            if prefix in task.id:
                count += 1
        return "%s%d" % (prefix, count)

    @property
    def start_date(self) -> date:
        return min([task.start_date for task in self.project_tasks])


    @property
    def due_date(self) -> date:
        return max([task.due_date for task in self.project_tasks])


    def print_project_headers():
        print("\nProject Component Information:")


    def print_project(self):
        print("╔═Begin Project Component [%s] Information:" % (self.id))
        print("║\tName: %s - from %s to %s" % (self.name, self.start_date.strftime("%d/%m/%y"), self.due_date.strftime("%d/%m/%y")))
        print("║\tDescription: %s" % (self.description))
        ProjectTask.print_project_task_headers()
        for task in self.project_tasks:
            task.print_project_task()
        print("╚═End of Project Component [%s] Information" % (self.id))