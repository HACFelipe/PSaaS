from typing import List

from entity.building_block import BuildingBlock
from entity.project_task import ProjectTask

class Code(BuildingBlock):
    """Model for Code"""
    
    def __init__(self, description : str, linked_project_task : ProjectTask, source_code : str, testable : bool = False, expected_results : List[object] = None):
        super().__init__(
            description=description,
            linked_project_task = linked_project_task,
            testable = testable)
        self.expected_results = expected_results
        self.source_code = source_code


    def print_building_block(self):
        print("║ %-4s ║ %-8s ║ %-30s ║ %-20s ║ %-9s ║ %-30s ║ %-30s ║" % (self.id, type(self).__name__, self.description, self.linked_project_task.id, self.testable, str(self.expected_results), self.source_code))