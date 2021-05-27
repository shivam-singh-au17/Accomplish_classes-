# Q-1 ) Recursive implementation of atoi() function:(5 marks)
# Atoi() function converts a string into an integer.
# eg:
# st = “1234” is a string.
# if we perform,
# st + 1
# this results in error since “st” is a string and 1 is an integer, and,
# st + “1”
# this will append 1 into 1234. Giving us 12341.
# write a function that converts the above variable ‘st’ into an integer (so that we
# can perform mathematical operations on it).
# Let’s call our function “myAtoiRecursive()”, it should,
# myAtoiRecursive(st) + 1
# should give us 1235 (that is 1234+1).
# Sample input:
# “1234”
# Sample output:
# 1234
# atoi() function stands for ASCII to integer conversion. It is a C function, but not present in python. Try to
# write a recursive code that implements atoi() in python.)



def stringToInt(str):

	if (len(str) == 1):
		return ord(str[0]) - ord('0');

	y = stringToInt(str[1:]);

	x = ord(str[0]) - ord('0');

	x = x * (10**(len(str) - 1)) + y;
	return (x);



myNum = "1235"
print("Given String: ", myNum)
print(type(myNum))


strToInt = stringToInt(myNum)
print("Reversed integer: ", strToInt)
print(type(strToInt))






# Q-2 ) Write a function that prints digits of a number from left to right , using
# recursion:(5 marks)
# Sample Input:
# 1234567
# Sample output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7





def leftToRight(num):
    if num < 10:
        print(num)
    else:
        leftToRight(num // 10)
        print(num % 10)


myNum = 1234567
leftToRight(myNum)






# Q-3 ) Reverse a string using recursion:(5 marks)
# If we have a string, write a function that prints reverse of that string, using
# recursion.
# Sample Input:
# ABCD
# Sample Output:
# DCBA


"""
name = 'Shivam'
print(name[-1])
print(name[-len(name)])

"""




def reverseString(str):
    if len(str) == 0:
        return str
    else:
        return reverseString(str[1:]) + str[0]


myStr = "ABCD"

print("Given String: ", myStr)

print("Reversed String: ", reverseString(myStr))





"""
Q-4 ) [Bonus Question] Recursive implementation of binary search:
(5 extra marks)

"""
# We have seen an iterative approach for binary search algorithm , write a
# recursive approach for that.
# HINT: when we divide the array into two parts, we need to perform a search on only one half.
# Apply binary search only on that half.

"""
Marks distribution:
Question 1,2 and 3 carry 5 marks each.
Question 4 is a bonus question, that means if you leave that question you dont lose a mark, but
if you solve it, you can extra 5 marks.
Remark: maximum marks you can get is 15, bonus question helps only of you are not able to
solve another question.

"""

