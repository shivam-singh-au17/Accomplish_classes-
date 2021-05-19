# Question 1 :
# ----------------
# Given a sorted Integer array , Write a Program to search the target
# element using Binary Search, If target element is found return the index .
# Otherwise return -1 .
# Input : arr = [1,2,3,15,16,19,23,55,1000] , target = 15
# Output: - 3
# Explanation:
# Just Use Binary search method
# Sample :
# def Binarysearch(arr , target):
# #write code here




def binarySearch(A, target):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == target:
            return mid
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__=="__main__":
    A = [1,2,3,15,16,19,23,55,1000]
    target = 15

    ans = binarySearch(A, target)
    print(ans)



#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(log N)             |
#    | Space Complexity  =  O(N)                 |
#    |                                           |
#    |___________________________________________|


# ----------------------------------------------------------------



# Questions:2
# Given an sorted integer array . Write a program to find Lower Bound of
# target number, return the index of the element
# Input: arr = [1,2 ,3,3,3,4,4,5,5,7,7,7] , target = 6
# Output: 8
# Explanation : -
# def Lower_Bound(arr , target):
# #write code here



def findLB(A, target):
    prev = -1
    for i in range(len(A)):
        if A[i] == target:
            return i
        elif A[i] > target:
            return prev
        prev = i


if __name__=="__main__":
    A = [1,2 ,3,3,3,4,4,5,5,7,7,7]
    target = 6

    ans = findLB(A, target)
    print(ans)




#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)             |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|


# ----------------------------------------------------------------




# Question : 3 -
# ------------------
# Given an sorted integer array . Write a program to find UPPER Bound of
# target number , return the index of the element .
# Input : - [1,2,2,2,3,3,5,5,5,6,6,7,7] , target = 7
# Output: - 12
# Explanation : HINT - already discussed in class;




def upperbound(A, target):
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
    A = [1,2,2,2,3,3,5,5,5,6,6,7,7]
    x = 7
    print(upperbound(A, x))
   


#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(log N)             |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|


# ----------------------------------------------------------------