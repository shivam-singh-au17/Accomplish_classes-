# 1. The Bedroom object has the following attributes:
# • length: length of the room in feet
# • breadth: breadth of the room in feet
# • height: breadth of the room in feet
# • bed: an object representing the bed in the bedroom. Initialize as None.
# • closet: an object representing the closet in the bedroom. Initialize as None.
# • has_balcony: True or False depending on whether the room has a balcony or not
# • has_window: True or False depending on whether the room has a window or not
# • num_lights: The number of lights/lightsockets in the number
# • has_ac: True or False depending on whether the room has a window or not
# • has_fan: True or False depending on whether the room has a window or not
# • num_charging_points: Number of charging points in the room.



# 2. The Bedroom object has the following methods:

# • carpet_area(): Returns the carpet area of the room which is calculated as length*breadth

# • add_bed(): creates a Bed object using user inputs [using input() function] and assigns it to the bed attribute of the bedroom. While adding a bed make sure the dimensions of the bed are suitable for the remaining carpet area in the room.

# For example: you cannot add a 9x9 bed in a 8X10 bedroom
# For example 2: you cannot add a 6x3 bed in a 8x10 bedroom if there is already a closet which takes up 60 sq ft space.

# • add_closet(): creates a Closet object using user inputs [using input() function] and assigns it to the closet attribute of the bedroom. While adding a close make sure the dimensions of the closet are suitable for the remaining carpet area in the room.

# For example: you cannot add a 9x9 closet in a 8X10 bedroom
# For example 2: you cannot add a 6x3 closet in a 8x10 bedroom if there is already a bed which takes up 60 sq ft space.

# • remove_bed(): Checks if the bed attribute is None. If not, then makes it None and returns “bed removed from the room”. If bed attribute is already None, then it returns “No bed found in the room”.

# • remove_closet(): Checks if the closet attribute is None. If not, then makes it None and returns “closet removed from the room”. If closet attribute is already None, then it returns “No closet found in the room”.




from bed import Bed
from closet import Closet


class Bedroom:
    def __init__(self, length, breadth, heigth, bed, closet, has_balcony,has_window, num_lights,has_ac, has_fan, has_charging_points):
        self.length = int(length)
        self.breadth = int(breadth)
        self.height = heigth
        self.bed = None
        self.closet = None
        self.has_balcony = has_balcony
        self.has_window = has_window
        self.num_lights = num_lights
        self.has_ac = has_ac
        self.has_fan = has_fan
        self.has_charging_points = has_charging_points



    def carpet_area(self):
        return (self.length * self.breadth)


    def add_bed(self):

        length = input('len of bed: ')
        bre = input('breadth of bed: ')
        year = input('enter the year made: ')
        posts = input('has posts?: ')
        headboard = input('has head board?: ')
        material  = input('material: ')

        self.bed = Bed(length, bre, year, posts, headboard, material)

  
    def add_closet(self):

        length = input('length: ')
        breadth = input('breadth: ')
        height = input('height: ')
        max_capacity = input('max_capacity: ')
        items = input('items: ')

        self.closet = Closet(length, breadth,height, max_capacity, items)
     

  
    def remove_bed(self):

        if self.bed != None:
            self.bed = None
            print("bed removed from the room") 
        elif self.bed == None:
            print("No bed found in the room")
      


    def remove_closet(self):
        if self.closet != None:
            self.closet = None
            print("closet removed from the room") 
        elif self.closet == None:
            print("No closet found in the room")


b_rm = Bedroom(44, 55, 66, None, 11, True, True, 14, True, False, 2)

# print(b_rm.length)
# print(b_rm.breadth)
# print(b_rm.height)
# print(b_rm.bed)
# print(b_rm.closet)
# print(b_rm.has_balcony)
# print(b_rm.has_window)
# print(b_rm.num_lights)
# print(b_rm.has_ac)
# print(b_rm.has_fan)
# print(b_rm.num_charging_points)

# result1 = b_rm.carpet_area()
# print(f"carpet area of the room is ", result1)
# b_rm.add_bed()
# b_rm.add_closet()
# b_rm.remove_bed()
# b_rm.remove_closet()
