# 1. The Bed Object has the following attributes:
# length: length of the bed in feet
# breadth: breadth of the bed in feet
# year_made: Year in which the bed was made
# has_headboard: True or False depending on whether the bed has a headboard or not
# has_posts: True or False depending on whether the bed has sideposts or not
# material: material is wood, steel, plywood and so on.




class Bed:
    def __init__(self, length, breadth, year_made,has_headboard, has_posts, material):
        self.length = float(length)
        self.breadth = float(breadth)
        self.year_made = year_made
        self.has_headboard = bool(has_headboard)
        self.has_posts = bool(has_posts)
        self.material = material

Bd = Bed(10, 10, 2000, False, False, 'wood')

# print(Bd.length)
# print(Bd.breadth)
# print(Bd.year_made)
# print(Bd.has_headboard)
# print(Bd.has_posts)
# print(Bd.material)


# 2. The Bed Object does not support any following methods

