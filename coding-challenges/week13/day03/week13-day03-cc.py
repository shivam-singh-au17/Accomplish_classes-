

"""
Q-1 ) Maximum path sum in matrix - solve with DP
https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1
(5 marks)
(Medium)
Given a NxN matrix of positive integers. There are only three possible moves
from a cell Matrix[r][c].
1. Matrix [r+1] [c]
2. Matrix [r+1] [c-1]
3. Matrix [r+1] [c+1]
Starting from any column in row 0 return the largest sum of any of the paths up to
row N-1.
Example 1:
Input: N = 2
Matrix = {{348, 391},
{618, 193}}
Output: 1009
Explaination: The best path is 391 -> 618.
It gives the sum = 1009.

"""





def findMaxPath(mat):

	res = -1
	for i in range(M):
		res = max(res, mat[0][i])

	for i in range(1, N):

		res = -1
		for j in range(M):

			if (j > 0 and j < M - 1):
				mat[i][j] += max(mat[i - 1][j],
								max(mat[i - 1][j - 1],
									mat[i - 1][j + 1]))

			elif (j > 0):
				mat[i][j] += max(mat[i - 1][j],
								mat[i - 1][j - 1])

			elif (j < M - 1):
				mat[i][j] += max(mat[i - 1][j],
								mat[i - 1][j + 1])

			res = max(mat[i][j], res)
	return res

N=4
M=6
mat = ([[ 10, 10, 2, 0, 20, 4 ],
		[ 1, 0, 0, 30, 2, 5 ],
		[ 0, 10, 4, 0, 2, 0 ],
		[ 1, 0, 2, 20, 0, 4 ]])
			
print(findMaxPath(mat))





"""
Q-2 ) Tiling a Rectangle with the Fewest Squares - Solve with DP
(5 marks)
(Easy-since we solved it in recursion topic)
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
Given a rectangle of size n x m, find the minimum number of integer-sided
squares that tile the rectangle.
Example 1:
Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:
Input: n = 5, m = 8
Output: 5

"""





class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m: return 1
        depth = [0]*m
        
        def fn(x): 
            nonlocal ans 
            if x < ans: 
                if min(depth) == n: ans = x # all tiled
                else: 
                    i = min(depth)
                    j = jj = depth.index(i) # (i, j)
                    while jj < m and depth[jj] == depth[j]: jj += 1
                    k = min(n - i, jj - j)
                    for kk in reversed(range(1, k+1)): 
                        for jj in range(j, j+kk): depth[jj] += kk
                        fn(x+1)
                        for jj in range(j, j+kk): depth[jj] -= kk
                            
        ans = max(n, m)
        fn(0)
        return ans 




"""
Q-3 ) Divisor Game (solve with DP)
Easy (5 marks)
https://leetcode.com/problems/divisor-game/
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player
makes a move consisting of:
● Choosing any x with 0 < x < n and n % x == 0.
● Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play
optimally.
Example 1:
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:
Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more
moves.

"""

class Solution:
	def divisorGame(self, N: int) -> bool:
		result=[False for i in range(N+1)]
		for i in range(2,N+1):
			for j in range(1,i):
				if i%j==0 and result[i-j]==False:
					result[i]=True
					break
		return result[N]

