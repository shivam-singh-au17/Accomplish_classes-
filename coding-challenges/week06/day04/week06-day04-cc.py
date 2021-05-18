# Question 1 :
# --------------
# https://leetcode.com/problems/rotate-array/
# class Solution3(object):




class Solution:
    def rotate(self, nums):
      
        count = 0
        start = 0
        k = 3
        while count < len(nums):
            curr = start
            prev = nums[curr]
            while True:
                idx = (curr + k) % len(nums)
                nums[idx], prev = prev, nums[idx]
                curr = idx
                count += 1
                if start == curr:
                    break
            start += 1


# Time:  O(n)
# Space: O(1)





# Question : 2 -
# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        d_len = len(digits)
        for i in reversed(range(d_len)):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
                
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
        









