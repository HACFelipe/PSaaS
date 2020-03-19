from typing import List

from entity.project import Project

class ProjectList():
    """Model of ProjectList"""

    def __init__(self, projects : List[Project] = []):
        self.__projects = projects

    
    def add_project(self, project : Project):
        project.id = self.generate_id()
        self.__projects.append(project)


    def add_requirements(self, projects : List[Project]):
        for project in projects:
            self.add_project(project)


    def remove_project(self, project : Project):
        self.__projects.remove(project)
     

    def remove_projects(self, project : List[Project]):
        for project in projects:
            self.__projects.remove(project)


    def generate_id(self) -> str:
        prefix = "PC"
        count = 0
        for comp in self.__projects:
            if prefix in comp.id:
                count += 1
        return "%s%d" % (prefix, count)


    def print_projects(self):
        if self.__projects:
            Project.print_project_headers()
            for comp in self.__projects:
                comp.print_project()
        else:
            print("No Project Components defined!")

    @property
    def items(self):
        return self.__projects
