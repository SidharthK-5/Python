"""
Basic python class demo
"""

class Building:
    def __init__(self, color: str, no_of_floors: int):
        self.color = color
        self.no_of_floors = no_of_floors
    
    def describe(self):
        print("This building is {} and has {} floors.".format(self.color, self.no_of_floors))

first_building = Building("blue", 20)
first_building.describe()