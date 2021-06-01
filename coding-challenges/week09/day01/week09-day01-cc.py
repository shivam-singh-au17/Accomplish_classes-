
"""
Solve following questions with the help of recursion:
Q-1 ) Check if a number is Palindrome: (5 marks)
Given an integer, write a function that returns true if the given number is
palindrome, else false.
For example,
Sample input:
12321
Sample output:
palindrome
eg2:
Sample input:
1451
Sample output:
not palindrome.

"""





def findPalindrome(n, temp):
	if (n == 0):
		return temp;
	temp = (temp * 10) + (n % 10);
	return findPalindrome(n / 10, temp);



if __name__ == "__main__":

    n = 121;
    temp = findPalindrome(n, 0);

    if (temp != n):
        print("Palindrome");
    else:  
        print("Not Palindrome");





"""
Q-2 ) Program for Sum of the digits of a given number:(5 marks)
Sample Input:
1234567
Sample output:
28

"""





def sumOfDigits(num):
	if num == 0:
		return 0
	return (num % 10 + sumOfDigits(int(num / 10)))



if __name__ == "__main__":

    num = 1234567
    result = sumOfDigits(num)
    print("Sum of digits in",num,"is", result)





"""
Q-3 ) Given a number n, find sum of first n natural numbers:(5 marks)
Examples :
Input : 5
Output : 15
Explanation : 1 + 2 + 3 + 4 + 5 = 15
Input : 7
Output : 28
Explanation : 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

"""





def productNum(num):
	if num == 0:
		return 0
	return (num + productNum(int(num - 1)))



if __name__ == "__main__":

    num = 5
    result = productNum(num)
    print("Sum of first n natural",num,"is", result)





"""
Q-4 ) [Bonus Question] Given two number x and y, find product using
recursion.
(3 extra marks)
Examples :
Input : x = 5, y = 2
Output : 10
Input : x = 100, y = 5
Output : 500
(Hint: x * y = x+x+x+...y times…+x)

"""




def productNum( num , n ):
	if num < n:
		return productNum(n, num)
	elif n != 0:
		return (num + productNum(num, n - 1))
	else:
		return 0



if __name__ == "__main__":
    
    num = 5
    n = 2
    result = productNum(num, n)
    print("Product of", n, "x", num,"is", result)





"""
Marks distribution:
Question 1,2 and 3 carry 5 marks each.
Question 4 is a bonus question, that means if you leave that question you dont lose a mark, but
if you solve it, you can get an extra 3 marks.
Practise questions carry no marks, they are just for revision of concepts.
Remark: maximum marks you can get is 15, bonus question helps only of you are not able to
solve another question.
Practise questions (zero marks):
Q - 1) Rat in a Maze
https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
Q-2) Given a 3 x n board, find the number of ways to fill it with 2 x 1
dominoes.
https://www.geeksforgeeks.org/tiling-with-dominoes/
Q-3) Find factorial of a number.
Q-4) Find nth number in fibonacci series.

"""