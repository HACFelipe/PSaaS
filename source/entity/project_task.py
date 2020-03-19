from typing import List
from datetime import date
from entity.requirement import Requirement

class ProjectTask():
    """Model of ProjectTask"""

    def __init__(self, description : str, start_date : date, due_date : date, linked_requirements : List[Requirement]):
        self.__has_child = False
        self.id = ""
        self.description = description
        self.__start_date = start_date
        self.__due_date = due_date
        self.linked_requirements = linked_requirements
        self.project_subtasks : List["ProjectTask"] = []

      
    def add_subtask(self, subtask: "ProjectTask"):
        self.__has_child = True
        subtask.id = self.generate_id()
        self.project_subtasks.append(subtask)


    def generate_id(self) -> str:
        prefix = self.id + "PS"
        count = 0
        for subtask in self.project_subtasks:
            if prefix in subtask.id:
                count += 1
        return "%s%d" % (prefix, count)

    def print_project_task_headers():
        print("║\tTasks:")

    def print_project_task(self, level : int = 0):
        print("║\t%s[%s] - %s - from %s to %s" % ("\t" * level, self.id, self.description, self.start_date.strftime("%d/%m/%y"), self.due_date.strftime("%d/%m/%y")))
        if self.has_child:
            for subtask in self.project_subtasks:
                subtask.print_project_task(level + 1)


    @property
    def start_date(self):
        return self.__start_date


    @start_date.setter
    def start_date(self, value):
        self.__start_date = value


    @property
    def due_date(self):
        return self.__due_date


    @due_date.setter
    def due_date(self, value):
        self.__due_date = value


    @property
    def has_child(self):
        return self.__has_child