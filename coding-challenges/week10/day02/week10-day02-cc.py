

"""
Q-1 )Find the Duplicate Number:
https://leetcode.com/problems/find-the-duplicate-number/
(Solve the above using both the approaches discussed in class) and comment on
time
complexity.
:(5 marks)
Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only
constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

"""





# 1st mathod
"""
def findDuplicate(nums):

        count = [0] * (len(nums)+1)
       
        for val in nums:
            count[val] = count[val] + 1
            print(count)
        for i in range(len(count)):
            if count[i] > 1:
                return i


if __name__ == "__main__":

    nums = [1,3,4,2,2]
    ans = findDuplicate(nums)
    print(ans)

"""


# 2nd mathod

def findDuplicate(nums):
    first = nums[0]
    second = nums[nums[0]]
   
    while first != second: 
        first = nums[first]
        second = nums[nums[second]]
    first = 0
    while first != second: 
        first = nums[first] 
        second = nums[second]
    return first

if __name__ == "__main__":

    nums = [1,3,4,2,2]
    ans = findDuplicate(nums)
    print(ans)





"""
Q-2 )Sum of Unique Elements:
https://leetcode.com/problems/sum-of-unique-elements/
(5 marks)
You are given an integer array nums. The unique elements of an array are the elements that appear
exactly once in the array.
Return the sum of all the unique elements of nums.
Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

"""





def sumOfUnique(nums):

    hashDic = {}
    for i in nums:
        if i in hashDic.keys():
            hashDic[i] += 1
        else:
            hashDic[i] = 1

    sum = 0
    for k, v in hashDic.items():
        if v == 1: sum += k
    return sum


if __name__ == "__main__":

    nums = [1,2,3,2]
    ans = sumOfUnique(nums)
    print(ans)






"""
Q-3 ) Longest Common Prefix:
https://leetcode.com/problems/longest-common-prefix/submissions/
(5 marks)
Write a function to find the longest common prefix str amongst an array of
strings.
If there is no common prefix, return an empty str "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

"""






def longestCommonPrefix(strs):

    if not strs:
        return ""

    newStr = sorted(strs)
    for i in range(len(newStr[0])):

        for str in (newStr[1:]):

            if (str[i] != newStr[0][i]) or (i >= len(str)):
                return newStr[0][:i]

    return newStr[0]


if __name__ == "__main__":

    strs = ["flower","flow","flight"]
    ans = longestCommonPrefix(strs)
    print(ans)




