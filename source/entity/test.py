from typing import Type

from entity.building_block import BuildingBlock
from entity.code import Code
from entity.concept import Concept
from entity.executor import Executor

class Test():
    """Model for Test"""

    def __init__(self, linked_building_block : Type[BuildingBlock], executor : Executor, test_parameters : str = None):
        self.id = ""
        self.linked_building_block = linked_building_block
        self.executor = executor
        self.test_parameters = test_parameters
        self.results = []
        self.success = False

    def test_building_block(self):
        if self.linked_building_block.testable:
            if type(self.linked_building_block) == Code:
                code = self.linked_building_block
                print("\nTesting Code [%s]" % (code.id))
                results = self.executor.execute(code)
                self.results = results
                self.success = (code.expected_results == results)
            elif type(self.linked_building_block) == Concept:
                concept = self.linked_building_block
                print("\nTesting Concept [%s]" % (concept.id))
                print("Definition of [%s]: %s" % (concept.id, concept.concept_definition))
                results = input("To validate this concept, please type 1 and hit Enter.")
                self.results = results
                self.success = (results == "1")


    def print_test_headers():
        print("\nTest Information:")
        print("║ %-4s ║ %-7s ║ %-22s ║ %-18s ║ %-45s ║ %-35s ║ %-9s ║" % ("Id", "Type", "Linked Building Block", "Executor Language", "Parameters", "Result", "Success"))


    def print_test(self):
        print("║ %-4s ║ %-7s ║ %-22s ║ %-18s ║ %-45s ║ %-35s ║ %-9s ║" % (self.id, type(self.linked_building_block).__name__, self.linked_building_block.id, self.executor.language, self.test_parameters, str(self.results), self.success))
