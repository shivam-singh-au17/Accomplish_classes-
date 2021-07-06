

"""
Q-1 ) Diameter of a binary tree
https://leetcode.com/problems/diameter-of-binary-tree/description/
(5 marks)
(Easy)
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges
between them.
Example 1:
￼
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].

"""





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ptr = 0
        def recursion(root):
            if not root:
                return 0
            l = recursion(root.left)
            r = recursion(root.right)
            if l+r>self.ptr:
                self.ptr = l+r
            return 1+max(l,r)
        recursion(root)
        return self.ptr






"""
Q-2) Find the Town Judge (5 marks)
https://leetcode.com/problems/find-the-town-judge/
(Easy)
In a town, there are n people labelled from 1 to n. There is a rumor that one of
these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person
labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.
Otherwise, return -1.
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

"""





class Solution:
    def findJudge(self, N, trust):
        
        if N == 1:
            return 1
        trust_score = [ 0 for _ in range(N+1) ]
        
        for p1, p2 in trust:
            
            trust_score[p1] -= 1
            
            trust_score[p2] += 1
            
        
        for person in range(1, N+1):
            if trust_score[person] == N-1:
                return person
        
        return -1





"""
Q-3) Find Center of Star Graph (5 marks)
https://leetcode.com/problems/find-center-of-star-graph/
(Easy)
There is an undirected star graph consisting of n nodes labeled from 1 to n. A
star graph is a graph where there is one center node and exactly n - 1 edges that
connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
that there is an edge between the nodes ui and vi. Return the center of the given
star graph.
Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other
node, so 2 is the center.

"""




class Solution:
    def findCenter(self, edges) -> int:
        dic = {}
        for i in edges:
            dic[i[0]] = dic.get(i[0],0) + 1
            dic[i[1]] = dic.get(i[1],0) + 1
        n = len(dic.keys())
        for i in dic.keys():
            if dic[i] == n-1:
                return i



