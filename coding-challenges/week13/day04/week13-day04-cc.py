

"""
Q-1 ) Is Subsequence
https://leetcode.com/problems/is-subsequence/
(7.5 marks)
(Easy)
Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.
A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

"""





class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if not s:
            return True
        if not t:
            return False
        for i in range(len(t)):
            if(j<len(s) and s[j]==t[i]):
                j+=1
            if(j==len(s)):
                return True
        return False





"""
Q-2 ) Count Unique Characters of All Substrings of a Given String (7.5
marks)
(Easy-since we solved it in recursion topic)
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of
-a-given-string/
Let's define a function countUniqueChars(s) that returns the number of unique
characters on s.
● For example if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique
characters since they appear only once in s, therefore
countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of
s.
Notice that some substrings can be repeated so in this case you have to count
the repeated ones too.
Example 1:
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

"""





class Solution:
    def uniqueLetterString(self, s: str) -> int:
        prev = ans = 0
        d = {}
        for i,c in enumerate(s):
            k, j = d.get(c,[-1,-1])
            prev = prev + (i - j) - (j - k)
            d[c] = [j,i]
            ans += prev
        return ans




        