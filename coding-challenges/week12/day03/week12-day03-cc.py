

"""
Q-1 ) write a program to take input a Binary tree and tell if that binary tree is
balanced or not?
https://leetcode.com/problems/balanced-binary-tree/
(5 marks)
(Easy)
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by
no more than 1.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if root==None:
            return True

        def is_leaf(node):
            if node.left == None and node.right==None:
                return True
            return False
        
        def get_height(node):

            if is_leaf(node):
                return 1

            left  = node.left
            right = node.right
       
            if left!=None:
                h_left  = get_height(left)
                left_val = left.val
       
                if h_left == -1:
                    return -1
   
            else:
                h_left = 0
                left_val = None
   
            if right!=None:
                h_right = get_height(right)
                right_val = right.val

                if h_right == -1:
                    return -1
 
            else:
                h_right = 0
                right_val = None

            if abs(h_left-h_right)>1:
                return -1

            return max(h_left, h_right)+1
        
        res = get_height(root)
        if res==-1:
            return False
        return True





"""
Q-2 )Write steps in heapify/percolate down method, and write time
complexity and space complexity analysis.(5 marks)
(Super Easy)

"""





heap = [111, 22, 33, 4, 15, 64, 7, 8, 9]


def heapsort():
    global heap

    while len(heap) != 0:
        print(heap[0])
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
        heapify(0)


def heapify(i):
    global heap

    left_idx = 2 * i + 1
    right_idx = 2 * i + 2

    if left_idx > len(heap) - 1 and right_idx > len(heap) - 1:
        return

    max_idx = i
    if left_idx < len(heap) and heap[max_idx] < heap[left_idx]:
        max_idx = left_idx

    if right_idx < len(heap) and heap[max_idx] < heap[right_idx]:
        max_idx = right_idx

    if max_idx != i:
        heap[max_idx], heap[i] = heap[i], heap[max_idx]
        heapify(max_idx)


if __name__ == "__main__":
    n = len(heap)

    for i in range(n - 1, -1, -1):
        heapify(i)

    heapsort()





"""
Q - 3) Merge Two Binary Trees (5 marks)
https://leetcode.com/problems/merge-two-binary-trees/
(Easy)
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two
trees are overlapped while the others are not. You need to merge the two trees
into a new binary tree. The merge rule is that if two nodes overlap, then sum
node values up as the new value of the merged node. Otherwise, the NOT null
node will be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees.
Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
Marks distribution:
Question 1 and 2 and 3 carry 5 marks each.

"""





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        if t1 and t2:

            newNode = TreeNode(t1.val+t2.val)
            newNode.left = self.mergeTrees(t1.left, t2.left)
            newNode.right = self.mergeTrees(t1.right, t2.right)

        elif t1:

            newNode = TreeNode(t1.val)
            newNode.left = self.mergeTrees(t1.left, None)
            newNode.right = self.mergeTrees(t1.right, None)

        else:

            newNode = TreeNode(t2.val)
            newNode.left = self.mergeTrees(None, t2.left)
            newNode.right = self.mergeTrees(None, t2.right)

        return newNode




