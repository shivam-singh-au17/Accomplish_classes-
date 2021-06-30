"""
Q-1 ) Climbing Stairs - solve without DP
https://leetcode.com/problems/climbing-stairs/
(5 marks)
(Easy)
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

"""





class Solution:

    def climbStairs(self, n: int) -> int:
        ot=[0,1]
        for i in range(1,n+1):
            s=ot[i-1]+ot[i]
            ot.append(s)

        return max(ot)


if __name__ =="__main__":
    ans = Solution





"""
Q-2 )Solve above question with DP (5 marks)

"""





class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1,1]
        if n>=2:
            for i in range(2,n+1):
                steps.append(steps[i-1] + steps[i-2])

        return steps[-1]


if __name__ =="__main__":
    ans = Solution





"""
Q-3 ) Longest Common Subsequence - Solve using DP
(5 marks)
https://leetcode.com/problems/longest-common-subsequence/
(Medium)
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the
remaining characters.
● For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both
strings.
Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is
3

"""


class Solution:

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:

        m = len(s1)
        n = len(s2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper(s1, s2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):

        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helper(s1, s2, i + 1, j, memo),
                    self.helper(s1, s2, i, j + 1, memo),
                )

        return memo[i][j]


if __name__ =="__main__":
    ans = Solution




    