# 1. The Bathroom Object has the following attributes:

# length: length of the closet in feet
# breadth: breadth of the closet in feet
# has_sink: True or False depending on whether the bathroom has a slab or not
# has_bathtub: True or False depending on whether the bathroom has a bathtub or not
# has_tap: True or False depending on whether the bathroom has a tap or not
# has_shower: True or False depending on whether the bathroom has a shower or not

# 2. The Bathroom Object supports the following methods:

# bathing(): checks if atleast any one of the tap, shower or sink are available
# and returns “Suitable for bathing”, if not available it returns “Unsuitable for bathing”




class Bathroom:
    def __init__(self,length, breadth, has_sink, has_bathtub, has_tap, has_shower):

        self.length = float(length)
        self.breadth = float(breadth)
        self.has_sink = bool(has_sink)
        self.has_bathtub = bool(has_bathtub)
        self.has_tap = bool(has_tap)
        self.has_shower = bool(has_shower)
     
    def bathing(self):
        if (self.has_sink == True or self.has_tap == True or self.has_shower == True ):
            return f"Suitable for bathing"
        else:
            return f"Unsuitable for bathing"


bath = Bathroom(10, 20, False, False, False, True)
result = bath.bathing()
print(result)
