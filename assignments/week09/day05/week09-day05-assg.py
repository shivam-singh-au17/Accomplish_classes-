

"""
#  Q - 1 ) Sort Array by Increasing Frequency (5 Marks)
# https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/
# Given an array of integers nums, sort the array in increasing order based on the
# frequency of the values. If multiple values have the same frequency, sort them in
# decreasing order.
# Return the sorted array.
# Example 1:
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a
# frequency of 3.

"""





from collections import Counter

def frequencySort(nums):
    d = Counter(nums)
    def check(x):
        return d[x]

    nums.sort(reverse = True)
    nums.sort(key = check)
    return nums

if __name__ == "__main__":

    A = [1,1,2,2,2,3]
    print(frequencySort(A))





"""
# Q- 2 ) Average Salary Excluding the Minimum and Maximum Salary (5
# marks)
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Given an array of unique integers salary where salary[i] is the salary of the
# employee i.
# Return the average salary of employees excluding the minimum and maximum
# salary.
# Example 1:
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000
# respectively.
# Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

"""





def average(salary):

    salary.remove(min(salary))
    salary.remove(max(salary)) 

    return sum(salary) / len(salary)

if __name__ == "__main__":

    salary = [4000,3000,1000,2000]
    print(average(salary))





"""
Q - 3 ) Valid Anagram (5 Marks):
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

"""





def check(str1, str2):
	
	if(sorted(str1)== sorted(str2)):
		print(True)
	else:
		print(False)		

if __name__ == "__main__":

    str1 ="anagram"
    str2 ="nagaram"
    check(str1, str2)





"""
Q - 4 ) [BONUS QUESTION] Sort Integers by The Power Value (5
Marks):
The power of an integer x is defined as the number of steps needed to transform
x into 1 using the following steps:
● if x is even then x = x / 2
● if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 -->
10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
Given three integers lo, hi and k. The task is to sort all integers in the interval [lo,
hi] by the power value in ascending order, if two or more integers have the same
power value, sort them by ascending order.
Return the k-th integer in the range [lo, hi] sorted by the power value.
Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform
into 1 using these steps and that the power of x is will fit in 32 bit signed integer.
Example 1:
Input: lo = 12, hi = 15, k = 2
Output: 13
Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 -->
2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval is sorted by the power value [12,13,14,15]. For k = 2 answer is the
second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in
ascending order. Same for 14 and 15.

"""




