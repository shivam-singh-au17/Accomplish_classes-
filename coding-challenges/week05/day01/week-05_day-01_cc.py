#                                         Beds, Closets and Bedrooms - 1
#                       Make 3 classes Beds, Closets and Bedrooms with the following specifications:


#    1. The Bed Object has the following attributes:

#    length:        length of the bed in feet
#    breadth:       breadth of the bed in feet
#    year_made:     Year in which the bed was made
#    has_headboard: True or False depending on whether the bed has a headboard or not
#    has_posts:     True or False depending on whether the bed has sideposts or not
#    material:      material is wood, steel, plywood and so on.

#    2. The Bed Object does not support any following methods
#    ___





class Beds:

    # Constructor
    def __init__(self, bed_length, bed_breadth, year_made, has_headboard, has_posts, bed_material):

    # attributes
        self.length = bed_length
        self.breadth = bed_breadth
        self.year_made = year_made
        self.has_headboard = has_headboard
        self.has_posts = has_posts
        self.material = bed_material
  
#   # method
    def display_content(self):
        print(f"Beds length is : {self.length}")

b_ed = Beds(55, 44, 2020, True, False, "wood")
print(b_ed.breadth)
print(b_ed.length)
print(b_ed.year_made)
print(b_ed.has_headboard)
print(b_ed.has_posts)
print(b_ed.material)





#    1. The Closet Object has the following attributes:
   
#    length:       length of the closet in feet
#    breadth:      breadth of the closet in feet
#    height:       breadth of the closet in feet
#    max_capacity: Total number of items that a closet supports
#    items:        The list of items in the closet. [All strings]

#    2. The Closet Object supports the following methods:

#    store_item(): Takes a string as input and adds it to the items list
#    fetch_item(): Returns the frontmost object in the items list
#    ____
print() # for space





class Closets:

    def __init__(self, closets_length, closets_breadth, closets_height, max_capacity, closets_items):

        self.length = closets_length
        self.breadth = closets_breadth
        self.height = closets_height
        self.max_capacity = max_capacity
        self.items = closets_items
        
    def store_item(self):
        item = input("Enter the string list separated by space: ")
        list1 = item.split(" ")
        self.items = list1
        print(self.items)

    def fetch_item(self):
        print(self.items[0])
    


c_lt = Closets(55, 44, 202, 11, ["pen", "papre", "book", "mouse"])
print(c_lt.length)
print(c_lt.breadth)
print(c_lt.height)
print(c_lt.max_capacity)
print(c_lt.items)

c_lt.store_item()
c_lt.fetch_item()






#    1. The Bedroom object has the following attributes:

#       • length:              length of the room in feet
#       • breadth:             breadth of the room in feet
#       • height:              breadth of the room in feet
#       • bed:                 an object representing the bed in the bedroom. Initialize as None.
#       • closet:              an object representing the closet in the bedroom. Initialize as None.
#       • has_balcony:         True or False depending on whether the room has a balcony or not
#       • has_window:          True or False depending on whether the room has a window or not
#       • num_lights:          The number of lights/lightsockets in the number
#       • has_ac:              True or False depending on whether the room has a window or not
#       • has_fan:             True or False depending on whether the room has a window or not
#       • num_charging_points: Number of charging points in the room.

#    2. The Bedroom object has the following methods:

#       • carpet_area():   Returns the carpet area of the room which is calculated as length*breadth
#       • add_bed():       creates a Bed object using user inputs [using input() function] and assigns 
#                          it to the bed attribute of the bedroom
#       • add_closet():    creates a Closet object using user inputs [using input() function] and assigns 
#                          it to the closet attribute of the bedroom
#       • remove_bed():    Checks if the bed attribute is None. If not, then makes it None and returns 
#                          “bed removed from the room”. If bed attribute is already None, then it returns 
#                          “No bed found in the room”.
#       • remove_closet(): Checks if the closet attribute is None. If not, then makes it None and returns 
#                          “closet removed from the room”. If closet attribute is already None, then it returns 
#                          “No closet found in the room”.
print() # for space





class Bedroom:

    def __init__(self, bedroom_length, bedroom_breadth, bedroom_height, bedroom_bed, bedroom_closet, bedroom_has_balcony, bedroom_has_window,
     bedroom_num_lights, bedroom_has_ac, bedroom_has_fan,  bedroom_num_charging_points):

        self.length = bedroom_length
        self.breadth = bedroom_breadth
        self.height = bedroom_height
        self.bed = bedroom_bed
        self.closet = bedroom_closet
        self.has_balcony = bedroom_has_balcony
        self.has_window = bedroom_has_window
        self.num_lights = bedroom_num_lights
        self.has_ac = bedroom_has_ac
        self.has_fan = bedroom_has_fan
        self.num_charging_points = bedroom_num_charging_points
   
    def carpet_area(self):
        area = self.length * self.breadth
        print(f"Bedroom area is {area}")
        

    def add_bed(self):
        addbed = (input("Enter Bed Number: "))
        self.bed = addbed
        bed_num = self.bed
        print(self.bed)
      

    def add_closet(self):
        addcloset = (input("Enter Closet Number: "))
        self.closet = addcloset
        print(self.closet)
        

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

print(b_rm.length)
print(b_rm.breadth)
print(b_rm.height)
print(b_rm.bed)
print(b_rm.closet)
print(b_rm.has_balcony)
print(b_rm.has_window)
print(b_rm.num_lights)
print(b_rm.has_ac)
print(b_rm.has_fan)
print(b_rm.num_charging_points)

b_rm.carpet_area()
b_rm.add_bed()
b_rm.add_closet()
b_rm.remove_bed()
b_rm.remove_closet()




