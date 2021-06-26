


"""
Q-1 ) Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
(5 marks)
(Easy)
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.
Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

"""





# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums) -> TreeNode:

        def rec(nums, start, end):
            if start <= end:

                mid = (start + end) // 2
                node = TreeNode(nums[mid])

                node.left = rec(nums, start, mid - 1)
                node.right = rec(nums, mid + 1, end)

                return node

        return rec(nums, 0, len(nums) - 1)





"""
Q-2 ) Invert Binary Tree (5 marks)
https://leetcode.com/problems/invert-binary-tree/
(Easy)
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

"""





# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
          
            root.left, root.right = root.right, root.left
            
            if root.left:
                self.invertTree( root.left )
            
            if root.right:
                self.invertTree( root.right )
            
            return root
        
        else:
            return None





"""
Q-3 ) Binary Tree Tilt (5 marks)
https://leetcode.com/problems/binary-tree-tilt/
(Easy)
Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left
subtree node values and all right subtree node values. If a node does not have a
left child, then the sum of the left subtree node values is treated as 0. The rule is
similar if there the node does not have a right child.
Example 1:
Input: root = [1,2,3]
Output: 1
Explanation:
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right
subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1

"""





# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findTilt(self, root: TreeNode) -> int:

        self.res = 0
        node = root
        def helper(node):

            if node==None:              
                return 0
            else:
                
                l = helper(node.left)
                r = helper(node.right)
                self.res+=abs(r-l)
                return r+l+node.val

        helper(node)
        return self.res




