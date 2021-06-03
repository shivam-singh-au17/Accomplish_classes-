
"""
Q-1 ) Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
(5 marks)
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique and you may return
the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

"""





def intersection(nums1, nums2):
    
    uniqueList = []
    nums1 = sorted(set(nums1))
    nums2 = sorted(set(nums2))
    
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            uniqueList.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]: 
            j += 1
        else: 
            i += 1
            
    return uniqueList


if __name__ == "__main__" :

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    ans = intersection(nums1, nums2)
    print(ans)





"""
Q-2 ) Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
(5 marks)
You are given two integer arrays nums1 and nums2, sorted in
non-decreasing order, and two integers m and n, representing the number
of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing
order.
The final sorted array should not be returned by the function, but instead
be stored inside the array nums1. To accommodate this, nums1 has a
length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.

"""





def merge(nums1, m, nums2, n):

	last = m + n - 1
	i, j = m - 1, n -1
    
	while last >= 0:
		if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
			nums1[last] = nums1[i]
			i -= 1
		else:
			nums1[last] = nums2[j]
			j -= 1
		last -= 1
	return nums1


if __name__ == "__main__" :

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    ans = merge(nums1, m, nums2, n)
    print(ans)





"""
Q-3 ) Sort Colors
https://leetcode.com/problems/sort-colors/submissions/
(5 marks)
Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red,
white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""





def sortColors(nums):
    
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__" :

    nums = [2,0,2,1,1,0]
    ans = sortColors(nums)
    print(ans)




