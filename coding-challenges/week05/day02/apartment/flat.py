# 1. The Flat has the following attributes:

# bed_rooms: a list of all the bedrooms in the house, initialize as empty list
# bath_rooms: a list of all the bathrooms in the house, initialize as empty list
# kitchens: a list of all the kitchens in the house, initialize as empty list
# owner_name: name of the flat owner, initialize as None
# current_renter: name of the current renter, initialize as None


# 2. The Flat Object supports the following methods:

# rent_out(): Checks if flat is already on rent, if not then it returns the rent of the flat which is calculated as 5*carpet_area per month. Then it asks the user whether they agree to pay that amount or not using input(), if they say Y/Yes/yes then take another input() as their name and set the current_renter attribute.

# PS: carpet area of the flat is the sum of carpet area of all the rooms in the house.
# change_owner(): Takes a name as input from the user and changes the owner of the flat to that person


# from bedroom import Bedroom




class Flat:
    def __init__(self, bed_rooms, bath_rooms, kitchens, owner_name, current_renter):

        self.bed_rooms = []
        self.bath_rooms = []
        self.kitchens = []
        self.owner_name = None
        self.current_renter = None


    def rent_out(self):
        add_bad_room = input('add bed room no?: ')
        add_bath_rooms = input('add bath room no?: ')
        add_kitchens = input('add kitchen no?: ')
        self.bed_rooms.append(add_bad_room)
        self.bath_rooms.append(add_bath_rooms)
        self.kitchens.append(add_kitchens)
        self.owner_name = input('Enter owner name: ')
        self.current_renter = input('Enter renter name: ')
        if self.current_renter == None:
            return 5 * self.Bedroom.carpet_area()
        


    def change_owner(self):
        if self.owner_name == None:
            new_owner = input('Enter New Owner Name: ')
            return new_owner
        


flt = Flat([], [], [], None, None)

result1 = flt.rent_out()
print(result1)

result2 = flt.change_owner()
print(result2)

