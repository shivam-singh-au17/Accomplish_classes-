
# Question 1 : -
#              Given a Square Matrix of Dimension NXM , find all Non-Diagonal
#              Elements which are prime Numbers .
#              Input : [ [1,2,3] , [4,5,6] , [7,8,9] ]
#              Output: - 2 , 3 , 7
# Explanation: -
#             The Non-diagonal elements are: 2, 3 ,4 ,6 ,7,8
#             So the prime numbers among them are : - [ 2,3,7 ]
#             Answer: - 2,3,7.
#             Sample :
#             Def func(Matrix):


mat = [ [1,2,3] , [4,5,6] , [7,8,9] ]

def func(m):
    row = len(m)
    col = len(m[0])
    result = []
    for i in range(row):
        for j in range(col):
            if i != j:
               result.append((m[i][j]))
    return result


def Prime_number(inp):
    prime_num = []
    for i in range(0, len(inp)):
        isPrime = True
        for j in range(2, inp[i]):
            if inp[i] % j == 0:
                isPrime = False
                break
        if inp[i] > 1 and isPrime == True:
            prime_num.append(inp[i]) 

    return prime_num


N = func(mat)
ans = Prime_number(N)
print(ans)




# --------------------------------------------------------------------------------------------------------


# Questions:2
# Given a integer array , find all the numbers which are palindrome:
# Note : -Palindromes are numbers when reversed will get the same as the
# original number.
# 121 - >palindrome , 123 → not a palindrome
# Input: [1 , 2 , 256 , 252 , 1441 , 969 ,2331]
# Output: [1 , 2 , 252 , 1441 , 969 ]






def palindromeNumbers(list_a):

	c = 0

	for i in list_a:			

		t = i
		rev = 0
		while t > 0:
			rev = rev * 10 + t % 10
			t = t // 10

		if rev == i:
			print (i)
			c = c + 1

	print()
	print ("Total palindrome nos. are", c )
	print()

def main():

	list_a = [10, 121, 133, 155, 141, 252]
	palindromeNumbers(list_a)

	list_b = [ 111, 220, 784, 565, 498, 787, 363]
	palindromeNumbers(list_b)					

if __name__=="__main__":
	main()	






# --------------------------------------------------------------------------------------------------------

# Question : 3 -
# ------------------
# Given an integer array , find all the numbers whose digit sum is even.
# Input : - [1 , 2 , 1111,56 ,22 ,89 ,100]
# Output: - [2 , 22 , 1111]
# Example : 2 -> digit sum = 2
# 22 -> digit sum = 4
# 1111 -> digit sum = 4



n = [1 , 2 , 1111,56 ,22 ,89 ,100]

def findNdigitNums(n, result="", diff=0):
    if n > 0:
        ch = ord('0')
        if result == "":
            ch = ord('1')
        while ch <= ord('9'):
            if n & 1:
                absdiff = diff + (ch - ord('0'))
            else:
                absdiff = diff - (ch - ord('0'))
            findNdigitNums(n - 1, result + chr(ch), absdiff)
            ch = ch + 1
    elif n == 0 and abs(diff) == 0:
        print(result, end=' ')
if __name__ == '__main__':
	n = 3  
 
findNdigitNums(n)




# ------------------------------------------------------------------------------------------------------

# Questions : 4 -
# Given an array of size n and a number k, find all elements that appear
# more than n/k times
# Input : k = 4 ,n=9 , A = [ 3 ,1, 2, 2, 2, 1, 4, 3, 3 ]
# Output: - [ 3 , 2]
# Explanation : - val = n/k = (9/4) = 2 (integer part)
# Now , take count of each element , we get
# Count of element 3 -> 3
# Count of element 1 -> 2
# Count of element 2 -> 3
# Count of element 4 -> 1
# Since 3 and 2 are only elements which are having count greater than 2 .



def moreThanNdK(arr, n, k):
	if (k < 2):
		return
	temp = [[0 for i in range(2)]
			for i in range(k)]
	for i in range(k - 1):
		temp[i][0] = 0
	for i in range(n):
		j = 0
		while j < k - 1:
			if (temp[j][1] == arr[i]):
				temp[j][0] += 1
				break
			j += 1
		if (j == k - 1):
			l = 0
			while l < k - 1:
				if (temp[l][0] == 0):
					temp[l][1] = arr[i]
					temp[l][0] = 1
					break
				l += 1
			if (l == k - 1):
				while l < k:
					temp[l][0] -= 1
					l += 1
	for i in range(k - 1):
		ac = 0 
		for j in range(n):
			if (arr[j] == temp[i][1]):
				ac += 1
		if (ac > n // k):
			print("Number:",
				temp[i][1],
				" Count:", ac)

if __name__ == '__main__':

	print("First Test")
	arr1 = [ 3 ,1, 2, 2, 2, 1, 4, 3, 3 ]
	size = len(arr1)
	k = 3
	moreThanNdK(arr1, size, k)



# ---------------------------------------------------------------------------------------------------------------------------


# Question 5 : -
#       Given an array arr[], find the maximum j – i such that arr[j] > arr[i] .
#          Input :- arr = [ 34, 8, 10, 3, 2, 80, 30, 33, 1]
#          Output : - 6 (j = 7, i = 1)

# Explanation : -
#       Since at index ( j = 6 and i = 1 ) , we get maximum ( j - i ) where arr[j] > arr[i]
#       Sample :
#       Def find_max ( arr ):
#       Note : -
#       Find Time and Space Complexity of each Question given - (1 - 5 )



def maxIndexDiff(arr, n):
	maxDiff = -1
	for i in range(0, n):
		j = n - 1
		while(j > i):
			if arr[j] > arr[i] and maxDiff < (j - i):
				maxDiff = j - i
			j -= 1

	return maxDiff

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)




