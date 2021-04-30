
#   Define a function factorial() with one input n. [The default value of n needs to
#   be 5]. Use the factorial() function and other inbuilt functions to find the 
#   maximum between the following:
#   1. 5!+3!-21 and 2!+4!+12
#   2. 26!+31! and 22!+35!
#   3. 21!+34!-15! and 31!+27!-19!
#   Hint: you can use the min() and max() inbuilt functions of python.




def factorial(n):
    fact = 1
    for num in range(1, n+1):
        fact = fact * num
    return fact


first = max((factorial(5) + factorial(3) - 21), (factorial(2) + factorial(4) + 12))
print(first)

second = max((factorial(26) + factorial(31)), (factorial(22) + factorial(35)))
print(second)

third = max((factorial(21) + factorial(34) - factorial(15)), (factorial(31) + factorial(27) - factorial(19)))
print(third)





# There is a sequence of numbers called the fibonacci numbers where each number 
# can be calculated as the sum of the last 2 numbers before it.
# 0,1,1,2,3,5,8,13,....
# In the above sequence you can see that the fourth number 2 is the sum of the 
# second and third number 1 and 1. The fifth number 3 is the sum of 2 (fourth 
# number) and 1 (third number) and so on.
# Read More Here on this: https://en.wikipedia.org/wiki/Fibonacci_number
# Write a function fibonacci(n) which returns the nth fibonacci number. This 
# should be calcuated using the while loop. The default value of n should be 10.
# fibonacci(1)
# >>>0
# fibonacci(2)
# >>>1
# fibonacci(3)
# >>>1
# fibonacci(4)
# >>>2
# fibonacci(5)
# >>>3
# Also find the maximum of:
# fibonacci(12)+fibonacci(10) and fibonacci(11)+fibonacci(11).




# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return  fibonacci(n -1) +  fibonacci(n -2)

# ans = fibonacci(7)
# print(ans)






def fibonacci(n):
    prveNum = 0
    currentNum = 1
    for i in range(1, n):
        prevPrevNum = prveNum
        prveNum = currentNum
        currentNum = prveNum + prevPrevNum
    return currentNum

ans = fibonacci(7)
print(ans)

last = max((fibonacci(12)+fibonacci(10)), (fibonacci(11)+fibonacci(11)))
print(last)




