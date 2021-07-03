

"""
Q-3 ) Pascal's Triangle (5 marks)
https://leetcode.com/problems/pascals-triangle/
(5 marks)
(Easy)
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
as shown:
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]

"""





class Solution:
    def generate(self, num: int):
        pasc = []
        c = 0
        while num > 0:
            if c == 0:
                pasc.append([1])
                num -= 1
                c += 1
            elif c == 1:
                pasc.append([1,1])
                num -= 1
                c += 1
            else:
                l = [1]
                for i in range(1, len(pasc[-1])):
                    l.append(pasc[-1][i-1] + pasc[-1][i])
                l.append(1)
                pasc.append(l)
                num -=1
        return pasc





"""
Q-2 ) Pascal's Triangle II (5 marks)
https://leetcode.com/problems/pascals-triangle-ii/
(Easy)
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's
triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
as shown:
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:
Input: rowIndex = 0
Output: [1]

"""





class Solution:
    def getRow(self, rowIndex: int):
        tri=[[1], [1,1]]
        for i in range(2, rowIndex+1):
            row=[None]*(i+1)
            row[0]=1
            row[i]=1
            for j in range(1,i):
                row[j]=tri[i-1][j]+tri[i-1][j-1]
            tri.append(row)
        return tri[rowIndex]






"""
Q-3) Best Time to Buy and Sell Stock (5 marks)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the
ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 =
5.
Note that buying on day 2 and selling on day 1 is not allowed because you must
buy before you sell.

"""





class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        high_buy = 0
        
        prices = prices[::-1]
        
        for price in prices:
  
            if price > high_buy:
                high_buy = price
     
            if high_buy - price > max_profit:
                max_profit = high_buy - price

        return max_profit




