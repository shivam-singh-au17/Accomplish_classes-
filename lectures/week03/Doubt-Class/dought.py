# Diamond in one loop.
# All formulas for pattern will have to be in terms of n (user input) and line number otherwise, when input changes, we will get bad patterns.

# we need to take a line number as input from the user and print a diamond in a single loop.
# n = 5

# //*//    ln = 1, num_stars = 1, num_spaces_os = 3-1, (halfway mark)-ln
# /***/    ln = 2, num_stars = 3, num_spaces_os = 3-2
# *****    ln = 3, num_stars = 5, num_spaces_os = 3-3

# we had a formula for increasing odd numbers, 2*ln-1

# /***/    ln = 4, 4 and 2 are also symmetric, num_spaces = 4-3
# //*//    ln = 5, 5 and 1 are symmetric, num_spaces = 5-3
# 5-3 = ln - halfway mark

# 2*2-1 = 2*(6-4)-1=2*(n+1-ln)-1
# 2*1-1 = 2*(6-5)-1=2*(5+1-5)-1 = 2*(n+1-ln)-1

# the number of stars is increasing till halfway, the number of spaces is decreasing till halfway - 1

# number of stars is decreasing from halfway to end, the number of spaces is increasing. - 2

# as we know line number is always increasing.

# how do we find half of a number: n
# (n//2+n%2)
# if n is even or n is odd:
# if n is even, it is perfectly divisible by 2, and the remainder will be zero.
# 12. 12//2+12%2 = 6+0 = 6
# if n is odd, it will never be divisible by 2, so we just need to find the quotient and reminder and add them.
# 5=2+1= (5//2)+(5%2)
# 5/2 = 2.5

#  first from 1 and 2, we realize that we need to split the pattern into 2 halves to find a formula.


# n = input("Enter in the total number of lines: ")
# n = int(n)
# for ln in range(1, n+1):
#   if ln <= (n//2+n%2):
#     print(" "*((n//2+n%2)-ln), end= "")
#     print("*"*(2*ln-1))
#   else:
#     if n%2 == 1:
#       print(" "*(ln-(n//2+n%2)), end= "")
#       print("*"*(2*(n+1-ln)-1))
#     else:
#       print(" "*(ln-(n//2+n%2)-1), end= "")
#       print("*"*(2*(n+1-ln)-1))


# a. Using break/continue on a nested loops of days and weeks (which you take as user input), skip out on the even days of all odd weeks.

# weeks = int(input("Enter the number of weeks: "))
# days = int(input("Enter the days in a week: "))
# for week in range(1, weeks+1):
#   for day in range(1, days+1):
#     if week%2==1 and day%2==0:
#       continue
#     print("Week-", week, " Day-", day)

# def factorial(n):
#   fact=1
#   return fact
#   for num in range(1, n+1):
#     fact = fact*num
#   return fact

# once a function returns something, code following it will not work.

# factorial_26 = factorial(26)

# a variable and a function cannot have the same name

# n = input("Enter a boolean: ")
# if n == "True":
#   n = True
# elif n == "False":
#   n = False
# else:
#   n = bool(n)

# 1    : the first number in line 1 is 1, line 1 has 1 number in total
# 21   : the first number in line 2 is 2, line 2 has 2 number in total
# 321  : the first number in line 3 is 3, line 3 has 3 number in total
# 4321 : the first number in line 4 is 4, line 4 has 4 number in total
# 1234
# 5555
# 5 - every digit you got = every digit you want
# 4+1-everydigit you got

# 54321: the first number in line 5 is 5, line 5 has 5 number in total
# 12345: what we got
# 54321: what we want
# 66666:
# 6-every digit you got= every digit you want
# 5+1-every digit you got

# so after checking every line, we replace 5 by ln
# ln+1-every digit you got
# ln+1-digit

# n = input("Enter in the maximum number of lines: ")
# n = int(n)
# for ln in range(1, n+1):
#   for digit in range(1, ln+1):
#     print(ln+1-digit, end="")
#   print()

# n = int(n)
# for ln in range(1, n+1):
  # digit = ln
  # while digit > 0:
  #   print(digit, end="")
  #   digit = digit -1
  # for digit in range(ln,0,-1):
  #   print(digit, end="")
  # print()

# here for ln = 1, digit loop ran 1 time
# here for ln = 2, digit loop ran 2 time
# here for ln = 3, digit loop ran 3 time
# here for ln = 4, digit loop ran 4 time

# age = 21

# if age >= 18:
#   pass

# if age>=15:
#   pass

# here we run both

# if age >= 15:
#   if age >= 18:
#     pass

# if age == 23:
#   print("21 code")
# elif age >=18:
#   print("18+ code")
# elif age >= 15:
#   print("15+ code")

# print("Sets of if: ")
# if age == 23:
#   print("21 code")
# if age >=18:
#   print("18+ code")
# if age >= 15:
#   print("15+ code")





 