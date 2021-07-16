

"""
Q-1 ) Minimum Moves to Equal Array Elements
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
(5 marks)
(Easy)
Given an integer array nums of size n, return the minimum number of moves
required to make all array elements equal.
In one move, you can increment n - 1 elements of the array by 1.
Example 1:
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments
two elements):
[1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]

"""





class Solution:
    def minMoves(self, nums) -> int:
        sum=0
        m = min(nums)
        i = nums.index(m)
        for j in range(len(nums)):
            if(i==j):
                continue
            else:
                sum = sum+nums[j]-nums[i]
        return sum





"""
Q-2) Longest Substring Without Repeating Characters (5 marks)
https://leetcode.com/problems/longest-substring-without-repeating-charact
ers/
(Medium)
Given a string s, find the length of the longest substring without repeating
characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p1 = p2 = m = 0
        
        while p2 < len(s):
            if s[p2] not in d:
                d[s[p2]] = True
                p2 += 1
                m = max(len(d), m)
            else:
                del d[s[p1]]
                p1 += 1
            
        return m





"""
Q-3) Minimum Operations to Reduce X to Zero (5 marks)
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
(Medium)
You are given an integer array nums and an integer x. In one operation, you can
either remove the leftmost or the rightmost element from the array nums and
subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is
possible, otherwise, return -1.
Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x
to zero

"""





class Solution:
    def minOperations(self, nums, x: int) -> int:
        if x == 0:
            return 0
        if min(nums)>x:
            return -1
        x_ = sum(nums)-x
        if x_==0:
            return len(nums)
        if x_<0:
            return -1
        
        start = 0
        max_len = 0
        tmp_sum = 0
        for end in range(len(nums)):
            tmp_sum += nums[end]
            if tmp_sum>x_:
                while tmp_sum >x_:
                    tmp_sum-=nums[start]
                    start+=1
            if tmp_sum == x_:
                max_len = max(max_len, end-start+1)
        return len(nums)-max_len




