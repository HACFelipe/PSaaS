from entity.building_block import BuildingBlock
from entity.project_task import ProjectTask

class Concept(BuildingBlock):
    """Model for Concept"""

    def __init__(self, description : str, linked_project_task : ProjectTask, concept_definition : str, testable : bool = False):
        super().__init__(
            description=description,
            linked_project_task = linked_project_task,
            testable = testable)
        self.concept_definition = concept_definition


    def print_building_block(self):
        print("║ %-4s ║ %-8s ║ %-30s ║ %-20s ║ %-9s ║ %-30s ║" % (self.id, type(self).__name__, self.description, self.linked_project_task.id, self.testable, self.concept_definition))