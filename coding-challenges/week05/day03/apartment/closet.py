# 1. The Closet Object has the following attributes:

# length: length of the closet in feet
# breadth: breadth of the closet in feet
# height: breadth of the closet in feet
# max_capacity: Total number of items that a closet supports
# items: The list of items in the closet. [All strings]

# 2. The Closet Object supports the following methods:

# store_item(): Takes a string as input and adds it to the items list
# fetch_item(): Returns the frontmost object in the items list



class Closet:
    def __init__(self,length, breadth, height, max_capacity, items):
        self.length = float(length)
        self.breadth = float(breadth)
        self.height = float(height)
        self.max_capacity = max_capacity
        self.items = ['pen', 'book', 'mobaile']


    def store_item(self):
        toAdd = input('what do you want to store? ')
        self.items.append(toAdd)
        return self.items

    def fetch_item(self):
        self.items.pop(0)
        return self.items


clt = Closet(10, 20, 30, 40, ['pen', 'book'])

# result1 =  clt.store_item()
# print(result1)
# result2 = clt.fetch_item()
# print(result2)