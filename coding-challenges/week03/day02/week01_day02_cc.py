
# a. Given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd and all even multiples from 2 to 20 if the number is even. Use both for loop and while loop.


# Using For Loop

num = int(input("Enter any number: "))

if num % 2 == 1:
    for i in range (1,22,2):
        print(i*num)
elif num % 2 == 0:
    for i in range (2,21,2):
        print(i*num)


# Using While Loop

if num % 2 == 1:
    i = 1
    while i <= 21:
        print(i * num)
        i = i + 2
elif num % 2 == 0:
    i = 2
    while i <=20:
        print(i * num)
        i = i + 2



# b. Given a number as input from the user, print a triangle. Use both for loop and while loop.


# Using For Loop

numb = int(input("Enter any number: "))

for i in range(1, numb):
  print("*"*i)
for i in range(numb, 0, -1):
    print("*"*i)


# Using While Loop

i = 1
while i < numb:
    print("*" * i)
    i = i + 1
i = numb
while i > 0:
    print("*" * i)
    i = i - 1


  

