

"""
Q-1 ) Squares of a Sorted Array:(5 marks) (easy)
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

"""





def SortedArray(nums):
    n = len(nums)
    i = 0  
    j = n - 1
    k = n - 1
    result = list(range(n)) 

    while i <= j:
        SqrNg = nums[i] * nums[i]
        SqrPo = nums[j] * nums[j]
        if SqrNg < SqrPo:

            result[k] = SqrPo
            j = j - 1
        else:
    
            result[k] = SqrNg
            i = i + 1
        k = k - 1

    return result


if __name__ == "__main__":

    nums = [-4,-1,0,3,10]
    res = SortedArray(nums)
    print(res)





"""
Q-2 ) Reverse String:(5 marks) (easy)
Write a function that reverses a string. The input string is given as an array of characters
s.
https://leetcode.com/problems/reverse-string/
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""





def reverseString(str):
    
    if not str or len(str) <= 1:
        return str
    
    left = 0
    right = len(str)-1
    
    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    return str


if __name__ == "__main__":

    s = ["h","e","l","l","o"]
    res = reverseString(s)
    print(res)





"""
Q-3 )Maximum Ascending Subarray Sum: (5 marks) (easy)
https://leetcode.com/problems/maximum-ascending-subarray-sum/
Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where left <= i < right,
numsi < numsi+1. Note that a subarray of size 1 is ascending.
Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

"""





def MaxAscendingSum(nums):
    count = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):

        if nums[i] > nums[i-1]:
            count += nums[i]
        else:
            count = nums[i]
        maxSum = max(maxSum, count)

    return maxSum


if __name__ == "__main__":

    nums = [10,20,30,5,10,50]
    res = MaxAscendingSum(nums)
    print(res)





"""
Q-4 ) [Bonus Question] Move Zeroes: (5 extra marks) (Medium)
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""





def MoveZeroes(nums):
    left = 0
    right = 0
    while right < len(nums):
        if nums[left] == 0:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        else:
            left += 1
            right += 1
    return nums





if __name__ == "__main__":

    nums = [0,1,0,3,12]
    res = MoveZeroes(nums)
    print(res)




