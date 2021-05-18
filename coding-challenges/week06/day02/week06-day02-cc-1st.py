# Write a program to PRINT numbers from 1 to N , with conditions :
# a) If number is divisible by 7 , print("HI")
# b) If number is divisible by 11 , print("BYE")
# c) If number divisible by both 7 and 11 , print ("HiBYE")
# Example : -
# N = 12
# Output :
# Hi
# BYE

n = 12

for i in range(1, n):
    if (i % 7):
        print("Hi")
    if (i % 11):
        print("BYE")
    if (i % 7) and (i % 11):
        print("HiBYE")
    break






# Also, find the Time complexity for the algorithm.

#    _____________________________________
#    |                                   |
#    |                                   |
#    |          ANS =   O(N)             |
#    |                                   |
#    |___________________________________|




