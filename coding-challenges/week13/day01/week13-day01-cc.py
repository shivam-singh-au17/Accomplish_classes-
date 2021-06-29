

"""
Q-1 ) Fibonacci Number - solve without DP
https://leetcode.com/problems/fibonacci-number/
(5 marks)
(Easy)
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding
ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

"""





def fib(N):

    res = [0, 1]
    if N == 0:
        return res[0]

    elif N==1:
        return res[1]

    for i in range(2, N+1):
        res.append(res[-1] + res[-2])  

    return res[-1]


if __name__=="__main__":

    n = 2
    ans = fib(n)
    print(ans)





"""
Q-2 )Solve above question with DP (5 marks)

"""





def fibo(no, dp):
    if no == 0:
        return 0
    
    if no == 1:
        return 1

    if dp[no] is not None:
        return dp[no]
        

    ans = fibo(no - 1, dp) + fibo(no - 2, dp)
    dp[no] = ans
    return ans

if __name__ == "__main__":
    dp = [None] * 10005
    print(fibo(135, dp))





"""
Q-3 )Pow(x, n) - Solve using DP (5 marks)
https://leetcode.com/problems/powx-n/
(Medium)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

"""





class Solution:
    def myPow(self, x: float, n: int) -> float:

        def function(base = x, exponent = abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f

if __name__ == "__main__":
   
    print()




    