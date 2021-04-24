# a. Write a program to take in 2 numbers as input and print their +, -, /,//, % and *


num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

addition = num1 + num2
print("Addition is: ", addition)

subtraction = num1 - num2
print("Subtraction is: ", subtraction)

division = num1 / num2
print("Division is: ", division)

integer_division = num1 // num2
print("Integer division is: ", integer_division)

mode = num1 % num2
print("Mode is: ", mode)

multiplication = num1 * num2
print("Multiplication is: ", multiplication)



# b. Write a program that takes in 2 numbers and returns true if they are divisible by each other. False otherwise.

numA = int(input("Enter number one: "))
numB = int(input("Enter number two: "))

result = (numA % numB == 0 and numB % numA == 0)
print(result)

