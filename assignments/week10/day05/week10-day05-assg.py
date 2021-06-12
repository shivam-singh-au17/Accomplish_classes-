

"""
Q-1 ) Given a list, Write a brute force approach without using stacks(using
for loops, so that you can appreciate the beauty of stacks) to find the just
larger element on the right of the element, for each element.
And for last element, since there is no element on the right give “None”:
(5 marks)
(Easy)
Example 1:
Input: [2,1,7,4,6,8,1,9]
Output: [7,7,8,6,8,9,9,None]

"""





def findMaxElm(nums):

    maxNum = []
    for i in range(0, len(nums)):

        if nums[i] == nums[len(nums) - 1]:
            maxNum.append(None)

        else:
            for j in range(i + 1, len(nums)):

                if nums[j] > nums[i]:
                    maxNum.append(nums[j]) 
                    break

    return maxNum


if __name__ == "__main__":

    nums = [2,1,7,4,6,8,1,9]
    ans = findMaxElm(nums)
    print(ans)





"""
Q-2 )Next Greater Element I: (5 marks)
https://leetcode.com/problems/next-greater-element-i/
(Medium)
(See doubt session recording today to use stack to solve this problem)
You are given two integer arrays nums1 and nums2 both of unique elements,
where nums1 is a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding
places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, return -1 for this number.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in
the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array
is 3.
For number 2 in the first array, there is no next greater number for it in the
second array, so output -1.

"""





def nextGreaterElmt(nums1, nums2):

    res = []
    stack = []
    mapObj = {}

    for n in nums2:
        while stack and n > stack[-1]:
            mapObj[stack.pop()] = n
        stack.append(n)

    while stack:
        mapObj[stack.pop()] = -1

    for n in nums1:
        res.append(mapObj[n])

    return res


if __name__ == "__main__":

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    ans = nextGreaterElmt(nums1, nums2)
    print(ans)



"""
Q-3 ) Build an Array With Stack Operations (5 marks)
https://leetcode.com/problems/build-an-array-with-stack-operations/
(Medium)
Given an array target and an integer n. In each iteration, you will read a number
from list = {1,2,3..., n}.
Build the target array using the following operations:
● Push: Read a new element from the beginning list, and push it in the array.
● Pop: delete the last element of the array.
● If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the
answer is unique.
Example 1:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation:
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
Marks distribution:
Question 1,2 and 3 carry 5 marks each.

"""



def buildArray(target, n):
    
    
    res = []
    if len(target) == 0:
        return []
    
    last = target[-1]
    for i in range(1, last + 1):
        
        if i in target:
            res.append("Push")
        else:
            res.append("Push")
            res.append("Pop")

    return res     


if __name__ == "__main__":

    target = [1,3]
    n = 3
    ans = buildArray(target, n)
    print(ans)




