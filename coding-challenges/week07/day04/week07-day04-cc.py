# Question 1 :
# ----------------
# Given a sorted array with Duplicates . Write a program to find LOWER
# BOUND of a TARGET using Binary search Method .
# Return Index corresponding the element of lower bound element.
# Example :
# Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
# Output : - 6
# def Lower_Bound(arr , target):
# #write code here



def lowerbound(A, target) -> int:
    n = len(A)

    left = 0
    right = n - 1
    
    ans = -1

    while left <= right:
        mid = (left + right) >> 1       # or (left + right) // 2
        if A[mid] == target:
            ans = mid
            right = mid - 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
    
    return ans



if __name__ == "__main__":
    A = [1,1,1,2,2,3,3,5,5,5,7,7]
    x = 2
    print(lowerbound(A, x))




#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(log N)             |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|




# --------------------------------------------------------------------------------------------------------

# Questions:2
# Given a sorted array with Duplicates . Write a program to find UPPER
# BOUND of a TARGET using Binary search Method .
# Return Index corresponding to the element of the upper bound element.
# Example :
# Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
# Output : - 7
# def Upper_Bound(arr , target):
# #write code here





def upperbound(A, target) -> int:
    n = len(A)

    left = 0
    right = n - 1
    
    ans = -1

    while left <= right:
        mid = (left + right) >> 1 # or (left + right) // 2
        if A[mid] == target:
            ans = mid
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
    
    return ans


if __name__ == "__main__":
    A = [1, 1, 1, 1, 2,2,2,2,2,2, 3, 3, 4, 5, 5]
    x = 2
    print(upperbound(A, x))




#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(log N)             |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|




# --------------------------------------------------------------------------------------------------------

# Questions:3
# Given an array with NO Duplicates . Write a program to find PEAK
# ELEMENT
# Return value corresponding to the element of the peak element.
# Example :
# Input : - arr = [2,5,3,7,9,13,8]
# Output : - 5 or 13 (anyone)
# HINT : - Peak element is the element which is greater than both
# neighhbours.
# def FindPeak(arr ):
# #write code here
# Write Time and Space Complexity of Questions(1-3).




def FindPeak(A):

    n = len(A)
    for i in range(0, n):
        if i ==0 and A[i+1] < A[i]:
            return A[i]
        if i == n-1 and A[i-1]< A[i]:
            return A[i]
        if A[i] > A[i-1] and A[i] > A[i+1]:
            return A[i]

if __name__ == "__main__":
    A = [2,5,3,7,9,13,8]
    print(FindPeak(A))


#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|