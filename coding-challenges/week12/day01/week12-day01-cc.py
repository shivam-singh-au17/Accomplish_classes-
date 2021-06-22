

"""
Q-1 ) Write a program to print nodes in a BST having odd values:
(Easy)
(5 marks)
Input:
Sample output:
3
1
7
13

"""





class newNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def inorder( root) :
	if (root != None):
		inorder(root.left)
		print(root.key, end = " ")
		inorder(root.right)
	

def insert(node, key):
	if (node == None):
		return newNode(key)

	if (key < node.key):
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	return node


def oddNode(root) :

	if (root != None):
		oddNode(root.left)
		
		if (root.key % 2 != 0):
			print(root.key, end = " ")
		oddNode(root.right)


if __name__ == '__main__':
	
	root = None
	root = insert(root, 5)
	root = insert(root, 3)
	root = insert(root, 2)
	root = insert(root, 4)
	root = insert(root, 7)
	root = insert(root, 6)
	root = insert(root, 8)

	oddNode(root)











"""
Q-2 ) Binary Search Tree to Greater Sum Tree (5 marks)
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
(Easy)
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus
sum of all keys greater than the original key in BST.
As a reminder, a binary search tree is a tree that satisfies these constraints:
● The left subtree of a node contains only nodes with keys less than
the node's key.
● The right subtree of a node contains only nodes with keys greater
than the node's key.
● Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 538:
https://leetcode.com/problems/convert-bst-to-greater-tree/
Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

"""





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root):
        s = 0
        def f(root):
            if root is None: return
            nonlocal s
            f(root.right)
            s = s + root.val
            root.val = s
            f(root.left)
        f(root)
        return root





"""
Q-3 ) Kth Smallest Element in a BST (5 marks)
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
(Medium)
Given the root of a binary search tree, and an integer k, return the kth
(1-indexed) smallest element in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
Marks distribution:
Question 1,2 and 3 carry 5 marks each
"""





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        
        stack = []
        count  = 0
        ans = -1
        while(count != k):
            while(root):
                stack.append(root)
                root = root.left            
            root = stack.pop()
            ans = root.val
            count += 1
            root = root.right
        return ans




