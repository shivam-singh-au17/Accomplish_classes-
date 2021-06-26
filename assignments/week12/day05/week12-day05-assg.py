


"""
Q-3 ) Top K Frequent Elements (5 marks)
https://leetcode.com/problems/top-k-frequent-elements/
(5 marks)
(Medium)
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]

"""





import heapq

class Solution:

    def topKFrequent(self, nums, k):
        
        h =[]
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1     

        for key,val in d.items():

            heapq.heappush(h,(val, key))     
            if len(h) > k:
                heapq.heappop(h)

        return [el[1] for el in h]





"""
Q-2 ) Lowest Common Ancestor of a Binary Search Tree (5
marks)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search
-tree/
(Easy)
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and
q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

"""





# Definition for a binary tree node.

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
           
            if root.val == p.val or root.val == q.val:
                return root

            if q.val > root.val and p.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)

            if q.val < root.val and p.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)

            if q.val > root.val and p.val < root.val or q.val < root.val and p.val > root.val:

                return root





"""
Q-3) Same Tree (5 marks)
https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function to check if they
are the same or not.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

"""





# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def check(p,q):

            if p is None and q is None:
                return True
            if (p is None and q is not None ) or (p is not None and q is None):
                return False
            if p.val!=q.val:
                return False

            return check(p.left,q.left) and check(p.right,q.right)

        return check(p,q)





"""
Q - 4) [BONUS QUESTION] Write a program to compute height of a perfect
Binary tree, and explain it’s time complexity.(4 marks)

"""