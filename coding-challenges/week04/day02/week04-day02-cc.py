#   Take 2 sequences of space separated integers as input from the user and convert 
#   it into a list of integers. Extend the first list with all the items of the 
#   second list and print the output.
#   Ex:
#   Input 1:
#   1 2 3 4
#   11 434 1
#   Output 1:
#   1 2 3 4 11 434 1
#   Input 2:
#   1 2 3
#   8 7
#   Output 2:
#   1 2 3 8 7
#   Hint: Consider using the inbuilt extend() function of lists in python




l1 = input("Enter the list as space separated numbers: ")
new_l1 = l1.split(" ")
for idx in range(0, len(new_l1)):
    new_l1[idx] = int(new_l1[idx])

l2 = input("Enter the list as space separated numbers: ")
new_l2 = l2.split(" ")
for idx in range(0, len(new_l2)):
    new_l2[idx] = int(new_l2[idx])
    
new_l1.extend(new_l2)
print(new_l1)




#    Accomplish the same task as Lists are US - 1 but without using the built-in 
#    extend() function of the list data type in python.
#    Ex:
#    Input 1:
#    1 2 3 4
#    11 434 1
#    Output 1:
#    1 2 3 4 11 434 1
#    Input 2:
#    1 2 3
#    8 7
#    Output 2:
#    1 2 3 8 7



ls1 = input("Enter the list as space separated numbers: ")
new_ls1 = ls1.split(" ")
for idx in range(0, len(new_ls1)):
    new_ls1[idx] = int(new_ls1[idx])

ls2 = input("Enter the list as space separated numbers: ")
new_ls2 = ls2.split(" ")
for idx in range(0, len(new_ls2)):
    new_ls2[idx] = int(new_ls2[idx])

last_l = new_ls1 + new_ls2

print(last_l)

