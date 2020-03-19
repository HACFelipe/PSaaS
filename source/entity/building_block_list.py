from typing import List, Type

from entity.building_block import BuildingBlock
from entity.code import Code
from entity.concept import Concept

class BuildingBlockList():
    """Model of BuildingBlockList"""

    def __init__(self, building_blocks : List[Type[BuildingBlock]] = []):
        self.__building_blocks = building_blocks

    
    def add_building_block(self, building_block : Type[BuildingBlock]):
        building_block.id = self.generate_id()
        self.__building_blocks.append(building_block)


    def remove_building_block(self, building_block : Type[BuildingBlock]):
        self.__building_blocks.remove(building_block)


    def generate_id(self) -> str:
        prefix = "BB"
        count = 0
        for block in self.__building_blocks:
            if prefix in block.id:
                count += 1
        return "%s%d" % (prefix, count)


    def print_building_blocks(self):
        if self.__building_blocks:
            BuildingBlock.print_building_block_headers()
            for block in self.__building_blocks:
                block.print_building_block()
        else:
            print("No Building Block Components defined!")


    @property
    def items(self):
        return self.__building_blocks