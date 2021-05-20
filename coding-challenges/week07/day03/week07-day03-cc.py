# Question 1 :
# ----------------
# Write the code and submit .
# https://leetcode.com/problems/binary-search/




def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__=="__main__":
    nums = [-1,0,3,5,9,12]
    target = 9

    ans = search(nums, target)
    print(ans)
        



# --------------------------------------------------------------------------------------------------------




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




# --------------------------------------------------------------------------------------------------------

