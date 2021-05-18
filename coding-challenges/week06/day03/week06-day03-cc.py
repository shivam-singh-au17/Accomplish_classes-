# Question 1 :
# ---------------
# Write a Program to swap values , without using 3rd variable .
# Also find Time and Space Complexity --- Marks : - 5
# Example : -
# Input : -
# A = 20 , B = 10
# Output : - A = 10 , B = 20
# Explanation : - values has been swapped
# Sample :
# Def swap(A,B):
# #write code here




        
def swap(A, B):
    if A != B:
        print(f"A = {B}, B = {A}")
    else:
        print(f"A = {B}, B = {A}")


swap(5, 5)



#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(A)+O(B)            |
#    | Space Complexity  =  O(2)                 |
#    |                                           |
#    |___________________________________________|







# Question : 2 -
# Given a number , find if the number is a perfect square root or not ? --- Marks :-5
# Also , find Time and space Complexity
# example :
# Input : n = 4
# output : - True
# Input : n = 10
# output : - False
# Explanation : since square root (4) =2 (perfect square ) --true
# Square root(10) = 3.35 (Not perfect square) -- false
# Sample :
# Def find_perfect_square(N):
# # write code here





def find_perfect_square(N):
    result = False
    for i in range(1, N+1):
        if (i * i == N):
            result = True
            break
        else:
            result = False

    if result == True:
        print(True)
    else:
        print(False)


find_perfect_square(16)



#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|







# Questions : 3 --
# Print prime numbers between 1 to N : ---marks: 5
# using for loop :
# Also , find the Time and Space complexity
# Example : -
# Input : - N = 10
# output : - [2 , 3 , 5 , 7 ]
# Explanation : - 2 , 3 , 5 , 7 are primes number between 1 to 10
# Sample :-
# Def Prime_number(N):
# write code here


N = int(input("Enter your num: "))

def Prime_number(inp):
    prime_num = []
    for i in range(1, inp):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if i > 1 and isPrime == True:
            prime_num.append(i) 

    return prime_num

ans = Prime_number(N)
print(ans)





#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(M)                 |
#    |                                           |
#    |___________________________________________|



