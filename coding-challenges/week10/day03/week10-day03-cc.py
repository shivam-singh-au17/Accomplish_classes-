
"""
Q-1 ) Write a program to convert a string of binary number into a decimal
number: (5 marks)
(Easy)
eg:
Sample Input
st = “101”
Sample output
5
Revise the lecture to see the algorithm to convert binary to decimal

"""



def binaryToDecimal(binary):
	value = 0
	i = 0
	while(binary != 0):

		dec = binary % 10
		value = value + dec * pow(2, i)
		binary = binary // 10
		i += 1

	print(value)	
	


if __name__ == '__main__':

	binaryToDecimal(101)






"""
# Q-2 ) Number of 1 Bits: (5 marks)
# (Medium)
# https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and returns the number of '1' bits
# it has (also known as the Hamming weight).
# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has
# a total of three '1' bits.

"""





def Numberof1Bits(n):
    res = 0
    while n:
        res += n & 1
        n >>= 1

    return res


if __name__ == '__main__':

    n = input()
    ans = Numberof1Bits(n)
    print(ans)





"""
Q-3 )Write a function to perform XOR between two positive integers: (5
marks), do not use the xor operator.
(Easy)
Sample Input:
A = 5
B = 3
Sample Output:
A^B = 6
explanation:
Take two inputs A and B as integers. => A = 5 , B = 3
Convert them to binary, => A = 101, B = 011
perform XOR operation, => A^B = 110
return resultant binary number as decimal number . => (110)2 = (6)10

"""





def performXOR(x, y):
	res = 0 

	# Assuming 32-bit Integer
	for i in range(31, -1, -1):
		
		b1 = x & (1 << i)
		b2 = y & (1 << i)
		b1 = min(b1, 1)
		b2 = min(b2, 1)

		xorOP = 0
		if (b1 & b2):
			xorOP = 0
		else:
			xorOP = (b1 | b2)

		res <<= 1;
		res |= xorOP
	return res

if __name__ == '__main__':

    A = 5
    B = 3
    ans = performXOR(A, B)
    print(ans)




