from typing import List

class Requirement():
    """Model of Requirement"""

    def __init__(self, name : str, description : str, type : str):
        self.id = ""
        self.validated = False
        self.traceability : List["Requirement"] = []
        self.name = name
        self.description = description
        self.type = type


    def validate_requirement(self):
        self.validated = True


    def print_requirement_headers():
        print("\nRequirement Information:")
        print("║ %-4s ║ %-14s ║ %-29s ║ %-13s ║ %-9s ║" % ("Id", "Name", "Description", "Type", "Validated"))


    def print_requirement(self):
        print("║ %-4s ║ %-14s ║ %-29s ║ %-13s ║ %-9s ║" % (self.id, self.name, self.description, self.type, self.validated))


    def print_traceability_header():
        print("\nTraceability Information:")
        print("║ %-4s ║ %-14s ║ %-70s ║" % ("Id", "Name", "Traceability"))


    def print_traceability(self):
        print("║ %-4s ║ %-14s ║ %-70s ║" % (self.id, self.name, str([req.id for req in self.traceability])))