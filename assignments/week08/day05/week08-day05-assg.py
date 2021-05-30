
"""
Q - 1 ) Write a program to find the upper bound (first occurrence’s index) of
a target given by the user, that should be present in the list. Using linear
search.
eg:
A= [1,1,1,2,2,2,3,3,4]
lower bound of 2 = 3
upper bound of 2 = 5
Your code should return 5.
Write time and space complexity of your code.
(3 marks)

"""











"""
Q - 2 ) Solve question 1 , but use binary search search.
Write time and space complexity of your code.
(3 marks)

"""












"""
Q - 3 ) Find largest number in a list, and second largest number, (without
using inbuilt functions).
eg:
A = [1,3,4,5,8,1,2,3,4,9,6,9]
return 9 and 8.
Write time and space complexity of your code.
(3 marks)

"""



def findLargestNum(arr):
    bigNum = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > bigNum:
            bigNum = arr[i]

    return bigNum


def findLargIndex(arr):
    bigNum = arr[0]
    largeNumidx = 0
    for i in range(0, len(arr)):
        if arr[i] > bigNum:
            bigNum = arr[i]
            largeNumidx = i

    return largeNumidx


def secondLargNum(arr, index):
    secondbigNum = arr[0]
    for i in range(0, len(arr)):
        arr[index] = 0
        if arr[i] > secondbigNum:
            secondbigNum = arr[i]
           
    return secondbigNum




if __name__=="__main__":

    arr = [15, 3, 4, 5, 8, 11, 2, 10, 4, 9, 6, 19]

    result = findLargestNum(arr)
    print("largest number in a list:", result)

    index = findLargIndex(arr)

    result = secondLargNum(arr, index)
    print("second largest number in a list:", result)







"""
Q - 4 ) Check If N and Its Double Exist:
https://leetcode.com/problems/check-if-n-and-its-double-exist/
Given an array arr of integers, check if there exists two integers N and M such
that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
● i != j
● 0 <= i, j < arr.length
● arr[i] == 2 * arr[j]
Example :
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Write time and space complexity of your code.
(3 marks)

"""












"""
Q - 5 ) Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Write time and space complexity of your code.
(3 marks)

"""














"""
Q- 6 ) [BONUS QUESTION] (5 marks)
Solve question 5, but within O(nlogn) time complexity.

"""





