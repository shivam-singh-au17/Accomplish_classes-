# 1. The Kitchen has the following attributes:

# length: length of the bed in feet
# breadth: breadth of the bed in feet
# slab_material: whether the slab is granite, wood, marble and so on.
# has_sink: True or False depending on whether the kitchen has a sink or not
# has_slab: True or False depending on whether the kitchen has a slab or not
# furnishing_material: whether the material is wood, steel, plywood and so on.
# lpg_pipeline: True or False depending on whether the kitchen has an LPG pipeline or not

# 2. The Kitchen Object supports the following methods:

# cook(): Checks if lpg connection, slab and sink exist and returns “Kitchen can
# be used for cooking” . If these connections donot exist, returns “Kitchen
# unsuitable for cooking”




class Kitchen:

    def __init__(self,length, breadth, slab_material, has_sink,has_slab, furnishing_material,lpg_pipeline):

        self.length = float(length)
        self.breadth = float(breadth)
        self.slab_material = slab_material
        self.has_sink = bool(has_sink)
        self.has_slab = bool(has_slab)
        self.furnishing_material = furnishing_material
        self.lpg_pipeline = bool(lpg_pipeline)

    def cook(self):
        if (self.has_sink == True and self.has_slab == True and self.lpg_pipeline == True ):
            return f"Kitchen can be used for cookin"
        else:
            return f"Kitchen unsuitable for cooking"


kitch = Kitchen(10, 10, 'marble', True, True, 'plywood', True)
ans = kitch.cook()     
print(ans)





