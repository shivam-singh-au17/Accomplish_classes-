
# a. Define a function arithmetic_operation() which takes 2 numbers and operation name as input and performs an ope
# ration on them:
# * opname: "Add" - Then we add 2 numbers
# * opname: "Sub" - Then we subtract 2 numbers
# * opname: "Multiply" - Then we multiply 2 numbers
# * opname: "Divide" - Then we divide the 2 numbers
# Print the result of the operation and also return it. 





def arithmetic_operation(n, m):

    opname = str(input("Enter op name: "))

    if opname == "Add":
        print(n + m)
        return n + m
    elif opname == "Sub":
        print(n - m)
        return n - m
    elif opname == "Multiply":
        print(n * m)
        return n * m
    elif opname == "Divide":
        print((n / m))
        return n / m

op = arithmetic_operation(26, 35)
print(op)



# b. Redefine the same function with default values for numbers as 3 and 5 and opname as "Add". Use the same functi
# on to calculate 5+3-12+23 


def arithmetic_operation_default():

    opname = "Add"
    a = 3
    b = 5
    if opname == "Add":
        return a + b

opA = arithmetic_operation_default()

opB = arithmetic_operation(12, 23)
calculate = opA - opB
print(calculate)

