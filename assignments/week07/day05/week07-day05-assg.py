# Question 1 :
# --------------
# Given a number N , count number of SET bits (having 1) in binary format of number N.
# INPUT - 26
# OUTPUT : 3
# Explanation :
# N = 26 , binary value = 11010 , count of set bits (having value 1) = 3.
# HINT : - Make use of bit manipulation concept .
# https://leetcode.com/problems/number-of-1-bits/ --- submit here



class Solution(object):
    def hammingWeight(self, n):

        list_bit=[];
        num=0;
        for i in range(33):
           num=2**i;
           list_bit.append(num); 

        count=0;
        for i in reversed(list_bit):
            if(n>=i):
               n=n-i;
               count+=1;
               
        return count;
            

#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|




# ---------------------------------------------------------------------------------------------------------------------------
# Question : 2 -
# https://leetcode.com/problems/sqrtx/



class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 0
        end = x
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        
        if end * end == x:
            return end
        
        return start


#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(logN)              |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|




# ---------------------------------------------------------------------------------------------------------------------------
# Q3.
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/



def findFirstAndLast(arr, n, x) :
	first = -1
	last = -1
	for i in range(0, n) :
		if (x != arr[i]) :
			continue
		if (first == -1) :
			first = i
		last = i
	
	if (first != -1) :
		print( "First Occurrence = ", first,
			" \nLast Occurrence = ", last)
	else :
		print("Not Found")
		
		

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
n = len(arr)
x = 8
findFirstAndLast(arr, n, x)
	

#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|




# ---------------------------------------------------------------------------------------------------------------------------
# Q4.
# Write a program to compute the power of a number.
# Input - x = 10 , y = 5 , calculate = (x^y)
# Output : - 100000
# Example -
# pow(n, 5) will give you n to the power 5. Use recursion in it.
# def pow(x,y):
# #write code here



base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))





#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(1)                 |
#    |                                           |
#    |___________________________________________|




# --------------------------------------------------------------------------------------------------------------------------
# Q5.
# https://leetcode.com/problems/majority-element/ .



class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]



#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(logn)              |
#    | Space Complexity  =  O(N)                 |
#    |                                           |
#    |___________________________________________|




# ---------------------------------------------------------------------------------------------------------------------------

