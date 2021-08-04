"""
"""
from random import randint


"""
1ST STEP:
Here first I have created a class named swiggy And here I have created 
three restaurants and given five items to each restaurant.

"""

class swiggy():

    def __init__(self):
        print()
        print("#"*25 ,"HELLO, WELCOME TO SWIGGY RESTAURANT", "#"*25)
        
        global res, Biraj_International, Grill_Inn, Pizzaria, dic, history 
        
        Biraj_International = {  
            "Paneer Chilli" : 170, 
            "Paneer Tikka" : 250, 
            "Mix Veg      " : 140, 
            "Malai Kofta" : 180, 
            "Shahi Kofta" : 180
            }

        Grill_Inn = {       
            "Surprise Burger" : 129, 
            "Grilled Sandwich" : 99, 
            "Paneer Wrap" : 169, 
            "Italian Sandwich" : 159, 
            "Pizza Puff     " : 129
            }

        Pizzaria = {      
            "Margherita Pizza" : 90, 
            "Veg Pizza    " : 90, 
            "Garlic Bread" : 99, 
            "Cheese Blast Pizza" : 289, 
            "Golden Corn Pizza" : 79
            }


        res = {
            "BIRAJ INTERNATIONAL": Biraj_International, 
            "GRILL INN": Grill_Inn, 
            "PIZZARIA": Pizzaria
            }

        dic = {}        # To store any item ordered by the user
        history = {}    # To see the history of any items ordered by the user at any restaurants.

        self.main_menu()
    





    """
    2ND STEP:
    Here I have created a function named main menu where any user can 
    order food, restaurants corner, exit and see their order history 
    and can select any of them option.

    """

    def main_menu(self):
        print("")
        print("="*35 ,"OUR  MAIN  MENU", "="*35)
        print()
        print("SELECT ANY ONE OF THESE AVAILABLE OPTIONS")
        print()
        print("(O) ORDER FOOD \n"
        "(R) RESTURANT CORNER \n"
        "(E) EXIT \n"
        "(H) ORDER HISTORY")
        print()
        print("="*86)
        while True:
            inp1 = input("PLEASE SELECT YOUR OPERATION: ").upper()
            if inp1 == 'O':
                self.restaurants()
                break
            elif inp1 == 'R':
                self.res_corner()
            elif inp1 == 'E':
                print("="*86)
                print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                print("="*86)
                exit()
            elif inp1 == 'H':
                self.History(history)
                break
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")





    """
    I created a function named restaurant where user can see all available 
    restaurants and can do anything to any of them and here this function is 
    doing this function when a user selects a restaurant then he can click 
    on that restaurant calls the function

    """

    def restaurants(self):

        print("="*86)
        print()
        print(">"*19,"WE HAVE THESE RESTAURANTS AVAILABLE THIS TIME:","<"*19)
        print()
        count = 1
        for i in res:
            print(str(count)+")", i)
            count += 1
        print()
        print("\n                           (M) MAIN MENU    (E) EXIT")
        print("="*86)
        while True:
            inp = str(input().upper())
            print("="*86)
            if inp == 'M':
                self.main_menu()
                break
            if inp == "E":
                print("="*86)
                print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                print("="*86)
                exit()
            try:
                if int(inp) == 1:
                    count = 1
                    for i in Biraj_International:
                        j = Biraj_International[i]
                        print("("+str(count)+")",i.upper(),"\t"*6,"price","\t","Rs","{:.2f}".format(float(j)))
                        count += 1
                    self.Biraj_International()
                    break   


                if int(inp) == 2:
                    count = 1
                    for i in Grill_Inn:
                        j = Grill_Inn[i]
                        print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                        count += 1
                    self.Grill_Inn()
                    break    

                if int(inp) == 3:
                    count = 1
                    for i in Pizzaria:
                        j = Pizzaria[i]
                        print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                        count += 1
                    self.Pizzaria()
                    break              
            except:
                print("INVALID INPUT PLEASE TRY AGAIN")





    """
    Here I have created a function in the name of a restaurant, there is a 
    different function for all restaurants and each restaurant's function 
    has some main options like exit to go to main menu and go to card and 
    The function of each restaurant has this facility that it can use all 
    the items available in that restaurant and whenever an item is 
    selected by a user, it is stored in the dictionary and it is also 
    accounted here. How many similar orders are being done by which scheme?

    """

    def Biraj_International(self):
        print()
        print("\n                     (M) MAIN MENU    (E) EXIT    (C)CART")
        print("="*86)
        dic = {}
        counter = 0
        qu = 0
        while True:
            inp = input("SELECT YOUR DESIRED CHOICE: ").upper()
            if inp == 'M':
                self.main_menu()

            if inp == 'E':
                print("="*86)
                print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                print("="*86)
                exit()

            if inp == "C":
                if counter < 4:
                    self.cart(dic,Biraj_International)
                    break
                else:
                    print("="*86)
                    print("RESTAURANT CANNOT PROCESS MORE THAN 3 ITEMS FOR ONE ORDER")
                    print("PLEASE TRY AGAIN")
                    self.main_menu()
                    break
            try:
                if qu <= 3:
                    if int(inp) == 1:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Paneer Chilli" not in dic:
                            dic["Paneer Chilli"] = inp1
                        else:
                            dic["Paneer Chilli"] += inp1
                        counter += inp1
                    if int(inp) == 2:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Paneer Tikka" not in dic:
                            dic["Paneer Tikka"] = inp1
                        else:
                            dic["Paneer Tikka"] += inp1
                        counter += inp1
                    if int(inp) == 3:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Mix Veg      " not in dic:
                            dic["Mix Veg      "] = inp1
                        else:
                            dic["Mix Veg      "] += inp1
                        counter += inp1
                    if int(inp) == 4:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Malai Kofta" not in dic:
                            dic["Malai Kofta"] = inp1
                        else:
                            dic["Malai Kofta"] += inp1
                        counter += inp1
                    if int(inp) == 5:
                        inp1 = int(input("HOW MANY DO YOU WANT: ")) 
                        if "Shahi Kofta" not in dic:
                            dic["Shahi Kofta"] = inp1
                        else:
                            dic["Shahi Kofta"] += inp1
                        counter += inp1
                else:
                    print("RESTURANT CANNOT PROCESS MORE THAN THREE ITEMS A TIME")   

            except:
                print("INVALID INPUT PLEASE TRY AGAIN--")





    """
    Here I have created a function in the name of a restaurant, there is a 
    different function for all restaurants and each restaurant's function 
    has some main options like exit to go to main menu and go to card and 
    The function of each restaurant has this facility that it can use all 
    the items available in that restaurant and whenever an item is 
    selected by a user, it is stored in the dictionary and it is also 
    accounted here. How many similar orders are being done by which scheme?

    """
    
    def Grill_Inn(self):
            print()
            print("\n                     (M) MAIN MENU    (E) EXIT    (C)CART")
            print("="*86)
            dic = {}
            counter = 0
            while True:
                inp = input("SELECT YOUR DESIRED CHOICE: ").upper()
                if inp == 'M':
                    self.main_menu()

                if inp == 'E':
                    print("="*86)
                    print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                    print("="*86)
                    exit()
                if inp == "C":
                    if counter < 4:
                        self.cart(dic,Grill_Inn)
                        break
                    else: 
                        print("="*86)
                        print("RESTAURANT CANNOT PROCESS MORE THAN 3 ITEMS FOR ONE ORDER")
                        print("PLEASE TRY AGAIN")
                        self.main_menu()
                        break
                try:
                    if int(inp) == 1:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Surprise Burger" not in dic:
                            dic["Surprise Burger"] = inp1
                        else:
                            dic["Surprise Burger"] += inp1
                        counter += inp1
                    if int(inp) == 2:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Grilled Sandwich" not in dic:
                            dic["Grilled Sandwich"] = inp1
                        else:
                            dic["Grilled Sandwich"] += inp1
                        counter += inp1
                    if int(inp) == 3:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Paneer Wrap" not in dic:
                            dic["Paneer Wrap"] = inp1
                        else:
                            dic["Paneer Wrap"] += inp1
                        counter += inp1
                    if int(inp) == 4:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Italian Sandwich" not in dic:
                            dic["Italian Sandwich"] = inp1
                        else:
                            dic["Italian Sandwich"] += inp1
                        counter += inp1
                    if int(inp) == 5:
                        inp1 = int(input("HOW MANY DO YOU WANT: ")) 
                        if "Pizza Puff     " not in dic:
                            dic["Pizza Puff     "] = inp1
                        else:
                            dic["Pizza Puff     "] += inp1
                        counter += inp1
                    

                except:
                    print("INVALID INPUT PLEASE TRY AGAIN")





    """
    Here I have created a function in the name of a restaurant, there is a 
    different function for all restaurants and each restaurant's function 
    has some main options like exit to go to main menu and go to card and 
    The function of each restaurant has this facility that it can use all 
    the items available in that restaurant and whenever an item is 
    selected by a user, it is stored in the dictionary and it is also 
    accounted here. How many similar orders are being done by which scheme?

    """
    
    def Pizzaria(self):
            print()
            print("\n                     (M) MAIN MENU    (E) EXIT    (C)CART")
            print("="*86)
            dic = {}
            counter = 0
            while True:
                inp = input("SELECT YOUR DESIRED CHOICE: ").upper()
                if inp == 'M':
                    self.main_menu()

                if inp == 'E':
                    print("="*86)
                    print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                    print("="*86)
                    exit()
                if inp == "C":
                    if counter < 4:
                        self.cart(dic, Pizzaria)
                        break
                    else:
                        print("="*86)
                        print("RESTAURANT CANNOT PROCESS MORE THAN 3 ITEMS FOR ONE ORDER")
                        print("PLEASE TRY AGAIN")
                        self.main_menu()
                        break
                    
                try:
                    if int(inp) == 1:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Margherita Pizza" not in dic:
                            dic["Margherita Pizza"] = inp1
                        else:
                            dic["Margherita Pizza"] += inp1
                        counter += inp1
                    if int(inp) == 2:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Veg Pizza    " not in dic:
                            dic["Veg Pizza    "] = inp1
                        else:
                            dic["Veg Pizza    "] += inp1
                        counter += inp1
                    if int(inp) == 3:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Garlic Bread" not in dic:
                            dic["Garlic Bread"] = inp1
                        else:
                            dic["Garlic Bread"] += inp1
                        counter += inp1
                    if int(inp) == 4:
                        inp1 = int(input("HOW MANY DO YOU WANT: "))
                        if "Cheese Blast Pizza" not in dic:
                            dic["Cheese Blast Pizza"] = inp1
                        else:
                            dic["Cheese Blast Pizza"] += inp1
                        counter += inp1
                    if int(inp) == 5:
                        inp1 = int(input("HOW MANY DO YOU WANT: ")) 
                        if "Golden Corn Pizza" not in dic:
                            dic["Golden Corn Pizza"] = inp1
                        else:
                            dic["Golden Corn Pizza"] += inp1
                        counter += inp1

                except:
                    print("INVALID INPUT PLEASE TRY AGAIN")
            




    """
    Here I have created a function called cart where the price of any item of 
    all the restaurants selected by the user is stored and if the price of 
    that card is above 300 and up to 300 then it will get a discount 
    of 15% If five hundred percent is above ₹ 500, then a discount 
    of 20% is given to him and the total value is told to him.

    """

    def cart(self,dic,name):

        print(">"*40, "CART", "<"*40)
        print()
        print('\t'+"-"*68)
        print('\t'*2, "   ITEM","                            ", "QUANTITY")
        print('\t'+"-"*68)
        s = 0
        order_no = randint(0,10000)
        if name == Biraj_International:
            d = "BIRAJ INTERNATIONAL"
        elif name == Grill_Inn:
            d = "Grill_Inn"
        elif name == Pizzaria:
            d = "Pizzaria"
        for i in dic:
            s += name[i]*dic[i]
            if name == Biraj_International:
                print('\t'*2, i.upper(),'\t'*4, dic[i])
            else:
                print('\t'*2, i.upper(),'\t'*3, dic[i])
        print('\t'+"-"*68)
        print('\t'*2,"  ","TOTAL", "\t"*4,s)
        if s > 500:
            s -= s * 0.20
            print('\t'*2,"  ","DISCOUNT", "\t"*4,"20%")
            print('\t'+"-"*68)
            print('\t'*2,"  ","TO PAY", "\t"*4,s)
            
        elif s > 300:
            s -= s * 0.15
            print('\t'*2,"  ","DISCOUNT", "\t"*4,"15%")
            print('\t'+"-"*68)
            print('\t'*2,"  ","TO PAY", "\t"*4,s)
        print("\n                      P(PAY)    (M) MAIN MENU    (E) EXIT")
        print("="*86)
        while True:
            inp = input("SELECT YOUR OPERATION: ").upper()
            if inp == 'M':
                self.main_menu()
                break
            elif inp == 'P':
                history[order_no] = [d , s]
                self.payment(s)
                break
            elif inp == 'E':
                exit()
            else:
                print("INVALID INPUT PLEASE TRY AGAIN@")








    def payment(self, s):
        print()
        print(">"* 27, "WELCOME TO THE PAYMENT GATEWAY", "<"*27)
        print()
        print("AMOUNT TO BE PAID FOR YOUR SWIGGY ORDER RS", s, "/-")
        print()
        print("AVAILABLE PAYMENT OPTIONS \n"
        "(C) CREDIT CARD \n"
        "(D) DEBIT CARD \n"
        "(N) NET BANKING \n"
        "(U) UPI \n"
        "(W) WALLETS \n"
        "(A) CASH ON DELIVERY")

        print("="*86)
        while True:
            inp = input().upper()
            if inp == "C" or inp == "D" or inp == "N" or inp == "U" or inp == "W":
                print("="*86)
                print()
                print("PAYMENT SUCCESSFULL")
                print("HURRAY, ORDER CONFIRMED")
                print()
                print("\n                 (H) ORDER HISTORY    (M) MAIN MENU    (E) EXIT")
                print("="*86)
                while True:
                    inp1 = input("SELECT YOUR OPERATION: ").upper()
                    if inp1 == "M":
                        self.main_menu()
                        break
                    elif inp1 == 'E':
                        exit()
                    elif inp1 == 'H':
                        self.History(history)
                        break
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")
                print("="*86)
                self.main_menu()
            elif inp == 'A':
                if s > 499:
                    print("CASH ON DELIVERY IS NOT AVAILABLE FOR ORDERS ABOVE 499")
                    print("TRY AGAIN WITH DIFFERENT OPTIONS")
                else:
                    print("="*86)
                    print()
                    print("PLEASE PAY THE AMOUNT TO THE DELIVERY PARTNER")
                    print("HURRAY, ORDER CONFIRMED")
                    print()
                    print("\n                 (H) ORDER HISTORY    (M) MAIN MENU    (E) EXIT")
                    print("="*86)
                    while True:
                        inp1 = input("SELECT YOUR OPERATION").upper()
                        if inp1 == "M":
                            self.main_menu()
                            break
                        elif inp1 == 'E':
                            exit()
                        elif inp1 == 'H':
                            self.History(history)
                        else:
                            print("INVALID INPUT PLEASE TRY AGAIN")
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")
        







    def History(self,history):
        print()
        print(">"*33, " ORDER HISTORY","<"*33)
        if len(history) == 0:
            print("NO ORDERS YET")
            print()
            print("(M) MAIN MENU \n"
            "(E) EXIT")
            print("="*86)
        else:
            for i in history:
                print("ORDER NUMBER = ", i)
                print("RESTURANT -",history[i][0])
                print("ORDER TOTAL =",history[i][1])
                print("-"*30)
                print("(M) MAIN MENU \n"
                "(E) EXIT")
                print("="*86)
        while True:
            r = input("SELECT A OPERATION: ").upper()
            if r == 'M':
                self.main_menu()
                break
            elif r == 'E':
                exit()
            else:
                print("INVALID INPUT TRY AGAIN")








    def res_corner(self):
        print()
        print(">"*25,"WELCOME TO SWIGGY PARTNER  PROGRAM","<"*25)
        print()
        count = 1
        for i in res:
            print(str(count)+")", i)
            count += 1
        print()
        print("="*86)
        while True:
            inp = input("SELECT YOUR RESTURANT: ")
            if int(inp) == 1:
                print("="*86)
                print()
                print("LOGIN SUCCESSFULL")
                print("WELCOME BIRAJ INTERNATIONAL")
                print()
                print("(1) UPDATE YOUR PRICES \n"
                "(2) MAIN MENU \n"
                "(3) EXIT")
                print("="*86)
                while True:
                    inp1 = input("SELECT A OPERATION: ")
                    if int(inp1) == 1:
                        print("="*86)
                        print()
                        count = 1
                        for i in Biraj_International:
                            j = Biraj_International[i]
                            print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                            count += 1
                        print()
                        print()
                        print("(M) MAIN MENU \n"
                        "(E) EXIT")
                        print("="*86)
                        while True:
                            w = input().upper()
                            if w == 'M':
                                "hello"
                                self.main_menu()
                            elif w == 'E':
                                exit()
                            try:
                                if int(w) == 1:
                                    print("="*86)
                                    print("ITEM -","Paneer Chilli")
                                    print("OLD PRICE -", Biraj_International["Paneer Chilli"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Biraj_International["Paneer Chilli"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 2:
                                    print("="*86)
                                    print("ITEM -","Paneer Tikka")
                                    print("OLD PRICE -", Biraj_International["Paneer Tikka"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Biraj_International["Paneer Tikka"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 3:
                                    print("="*86)
                                    print("ITEM -","Mix Veg      ")
                                    print("OLD PRICE -", Biraj_International["Mix Veg      "])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Biraj_International["Mix Veg      "] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 4:
                                    print("="*86)
                                    print("ITEM -","Malai Kofta")
                                    print("OLD PRICE -", Biraj_International["Malai Kofta"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Biraj_International["Malai Kofta"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                
                                if int(w) == 5:
                                    print("="*86)
                                    print("ITEM -","Shahi Kofta")
                                    print("OLD PRICE -", Biraj_International["Shahi Kofta"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Biraj_International["Shahi Kofta"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                    
                            except:
                                print("INVALID INPUT PLAESE TRY AGAIN")
                    elif int(inp1) == 2:
                        self.main_menu()
                        break
                    elif int(inp1) == 3:
                        exit()
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")

            elif int(inp) == 2:
                print("="*86)
                print()
                print("LOGIN SUCCESSFULL")
                print("WELCOME GRILL IN")
                print()
                print("(1) UPDATE YOUR PRICES \n"
                "(2) MAIN MENU \n"
                "(3) EXIT")
                print("="*86)
                while True:
                    inp1 = input("SELECT A OPERATION: ")
                    print()
                    if int(inp1) == 1:
                        print("="*86)
                        print()
                        count = 1
                        for i in Grill_Inn:
                            j = Grill_Inn[i]
                            print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                            count += 1
                        print()
                        print()
                        print("(M) MAIN MENU \n"
                        "(E) EXIT")
                        print("="*86)
                        while True:
                            w = input().upper()
                            if w == 'M':
                                "hello"
                                self.main_menu()
                            elif w == 'E':
                                exit()
                            try:
                                if int(w) == 1:
                                    print("="*86)
                                    print("ITEM -","Surprise Burger")
                                    print("OLD PRICE -", Grill_Inn["Surprise Burger"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Grill_Inn["Surprise Burger"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 2:
                                    print("="*86)
                                    print("ITEM -","Grilled Sandwich")
                                    print("OLD PRICE -", Grill_Inn["Grilled Sandwich"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Grill_Inn["Grilled Sandwich"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 3:
                                    print("="*86)
                                    print("ITEM -","Paneer Wrap")
                                    print("OLD PRICE -", Grill_Inn["Paneer Wrap"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Grill_Inn["Paneer Wrap"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 4:
                                    print("="*86)
                                    print("ITEM -","Italian Sandwich")
                                    print("OLD PRICE -", Grill_Inn["Italian Sandwich"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Grill_Inn["Italian Sandwich"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                
                                if int(w) == 5:
                                    print("="*86)
                                    print("ITEM -","Pizza Puff     ")
                                    print("OLD PRICE -", Grill_Inn["Pizza Puff     "])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Grill_Inn["Pizza Puff     "] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                    
                            except:
                                print("INVALID INPUT PLAESE TRY AGAIN")
                    elif int(inp1) == 2:
                        self.main_menu()
                        break
                    elif int(inp1) == 3:
                        exit()
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")

            elif int(inp) == 3:
                print("="*86)
                print()
                print("LOGIN SUCCESSFULL")
                print("WELCOME PIZZARIA")
                print()
                print("(1) UPDATE YOUR PRICES \n"
                "(2) MAIN MENU \n"
                "(3) EXIT")
                print("="*86)
                while True:
                    inp1 = input("SELECT A OPERATION: ")
                    if int(inp1) == 1:
                        count = 1
                        print("="*86)
                        print()
                        for i in Pizzaria:
                            j = Pizzaria[i]
                            print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                            count += 1
                        print()
                        print("(M) MAIN MENU \n"
                        "(E) EXIT")
                        print("="*86)
                        while True:
                            w = input().upper()
                            if w == 'M':
                                "hello"
                                self.main_menu()
                            elif w == 'E':
                                exit()
                            try:
                                if int(w) == 1:
                                    print("="*86)
                                    print("ITEM -","Margherita Pizza")
                                    print("OLD PRICE -", Pizzaria["Margherita Pizza"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Pizzaria["Margherita Pizza"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")


                                if int(w) == 2:
                                    print("="*86)
                                    print("ITEM -","Veg Pizza    ")
                                    print("OLD PRICE -", Pizzaria["Veg Pizza    "])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Pizzaria["Veg Pizza    "] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 3:
                                    print("="*86)
                                    print("ITEM -","Garlic Bread")
                                    print("OLD PRICE -", Pizzaria["Garlic Bread"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Pizzaria["Garlic Bread"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 4:
                                    print("="*86)
                                    print("ITEM -","Cheese Blast Pizza")
                                    print("OLD PRICE -", Pizzaria["Cheese Blast Pizza"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Pizzaria["Cheese Blast Pizza"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                
                                if int(w) == 5:
                                    print("="*86)
                                    print("ITEM -","Golden Corn Pizza")
                                    print("OLD PRICE -", Pizzaria["Golden Corn Pizza"])
                                    e = input("ENTER NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Pizzaria["Golden Corn Pizza"] = e
                                    print("="*86)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                    
                            except:
                                print("INVALID INPUT PLAESE TRY AGAIN")
                    elif int(inp1) == 2:
                        self.main_menu()
                        break
                    elif int(inp1) == 3:
                        exit()
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")

            else:
                print("INVALID INPUT PLEASE TRY AGAIN")

         


if __name__ == "__main__":
    swiggy()







