


"""
Q-1 ) N-Queens
https://leetcode.com/problems/n-queens-ii/
(5 marks)
(Medium)
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens
puzzle.
Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
Input: n = 1
Output: 1

"""





class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        def helper(row = 0, diag1 = set(), diag2 = set(), column = set()):
            if row == n:
                self.count += 1
            for col in range(n):
                if row - col not in diag1 and row + col not in diag2 and col not in column:
                    helper(row + 1, diag1.union({row - col}), diag2.union({row + col}), column.union({col}))
        helper()
        return self.count





"""
Q-2)Sum of All Subset XOR Totals (5 marks)
https://leetcode.com/problems/sum-of-all-subset-xor-totals/
(Easy)
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if
the array is empty.
● For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.
Note: Subsets with the same elements should be counted multiple times.
An array a is a subset of an array b if a can be obtained from b by deleting some
(possibly zero) elements of b.
Example 1:
Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

"""





class Solution:
    def subsetXORSum(self, nums) -> int:
        ans = 0
        for mask in range(1 << len(nums)): 
            val = 0
            for i in range(len(nums)): 
                if mask & 1 << i: val ^= nums[i]
            ans += val
        return ans 





"""
Q-3)All Paths From Source to Target (5
marks)
https://leetcode.com/problems/all-paths-from-source-to-target/
(Easy)
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
possible paths from node 0 to node n - 1, and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from
node i (i.e., there is a directed edge from node i to node graph[i][j]).
Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

"""




class Solution:
    def allPathsSourceTarget(self, graph):
        
        mem=[ [] for i in range(len(graph))]
        self.util(0,graph,mem)
        return mem[0]
    
    def util(self,node,graph,mem):

        if len(mem[node])>0:
            return mem[node]

        if(node == len(graph)-1):
            return [[len(graph)-1]]

        for i in range(len(graph[node])):

            temp=self.util(graph[node][i],graph,mem)


            for pth in temp:
                mem[node].append([node]+pth)

        return mem[node]



