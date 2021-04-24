# a. Take a number as input from the user, print its multiple of 2, 4, 6, 8, 10 if it is an odd number, if it is an even number then print its multiple of 1, 3, 5, 7 and 9.

num = int(input("Write any number: "))
if num % 2 == 1 :
    print(num * 2, num * 4, num * 6, num * 8, num * 10)

# elif num % 2 == 0 :
#     print(num * 1, num * 3, num * 5, num * 7, num * 9)          #(We can use any of these)

else:
    print(num * 1, num * 3, num * 5, num * 7, num * 9)




# b. Take a name, age and whether user has diabetes as user input and tell them from when can they start taking vaccines for COVID-19. [Hint: you can refer to the news for the timelines for each age group]

name = input("Write your name: ")
age = int(input("Write your age: "))
Health_issue = str(input("Write your health issue: "))

if Health_issue == "diabetes" :
    if age >= 18:
        print(name,"your age is",age,"you can stay some time and control your diabetes or start taking vaccines")
    elif age >= 65:
        print(name,"your age is",age,"you can start taking vaccines immediately but you can control your diabetes strictly.")
    elif age < 18:
        print(name,"your age is",age,"you can wait and control your diabetes and start taking vaccines but after",18 - age, "years")
else:
    if age >= 18:
        print(name,"your age is",age,"you can start taking vaccines for COVID-19.")
    elif age >= 65:
        print(name,"your age is",age,"you can start taking COVID-19 vaccines immediately.")
    elif age < 18:
        print(name,"your age is",age,"you can wait and start taking vaccines for COVID-19 but after",18 - age, "years")


