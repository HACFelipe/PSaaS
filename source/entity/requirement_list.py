from typing import List
from entity.requirement import Requirement

class RequirementList():
    """Model of RequirementList"""

    def __init__(self, requirements : List[Requirement] = []):
        self.__requirements = requirements

    
    def add_requirement(self, requirement : Requirement):
        requirement.id = self.generate_id(requirement)
        self.__requirements.append(requirement)


    def add_requirements(self, requirements : List[Requirement]):
        for requirement in requirements:
            self.add_requirement(requirement)


    def remove_requirement(self, requirement : Requirement):
        self.__requirements.remove(requirement)
     

    def remove_requirements(self, requirements : List[Requirement]):
        for requirement in requirements:
            self.__requirements.remove(requirement)


    def generate_id(self, requirement: Requirement) -> str:
        prefix = "UR"
        if requirement.type == "Functional":
            prefix = "FR"
        elif requirement.type == "Nonfunctional":
            prefix = "NF"
        elif requirement.type == "Domain":
            prefix = "DM"
        elif requirement.type == "Data":
            prefix = "DT"
        elif requirement.type == "Business Rule":
            prefix = "BR"
        count = 0
        for req in self.__requirements:
            if prefix in req.id:
                count += 1
        return "%s%d" % (prefix, count)


    def print_requirements(self):
        if self.__requirements:
            Requirement.print_requirement_headers()
            for requirement in self.__requirements:
                requirement.print_requirement()
        else:
            print("No requirements defined!")

    
    def print_requirements_traceability(self):
        if self.__requirements:
            Requirement.print_traceability_header()
            for requirement in self.__requirements:
                requirement.print_traceability()
        else:
            print("No requirements defined!")


    @property
    def items(self):
        return self.__requirements