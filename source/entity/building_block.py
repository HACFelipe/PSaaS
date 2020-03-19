from typing import List

from entity.project_task import ProjectTask

class BuildingBlock():
    """Model for BuildingBlock"""

    def __init__(self, description : str, linked_project_task : ProjectTask, testable : bool = False):
        self.id = ""
        self.description = description
        self.linked_project_task = linked_project_task
        self.testable = testable


    def print_building_block_headers():
        print("\nBuilding Block Information:")
        print("║ %-4s ║ %-8s ║ %-30s ║ %-20s ║ %-9s ║ %-30s ║ %-30s ║" % ("Id", "Type", "Description", "Linked Task", "Testable", "Expected Results/Definition", "Source Code (if exists)"))


    def print_building_block(self):
        print("║ %-4s ║ %-8s ║ %-30s ║ %-20s ║ %-9s ║" % (self.id, type(self).__name__, self.description, self.linked_project_task.id, self.testable))