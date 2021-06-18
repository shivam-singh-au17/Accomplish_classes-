

"""
(Maximum marks -15)
Q-1 ) Dry run the recursive function “reverse_LL_rec(head prev)” from the
code given below, take input provided in the code:
(5 marks)
(Super Easy)

"""



class Node:
    def __init__(self,x): # Initialize and create an empty node
        self.data = x
        self.next = None

def printList(head):
    cur = head         #This function is to print our tree it returns the value of all our trees one by one
    while cur!=None:
        print(cur.data, end = " ")
        cur = cur.next

new_head = None
def reverse_LL_rec(head,prev):
    global new_head
    if head is None:     # If our root is empty then come out of the function
        return
    if head.next is None:
        head.next = prev
        return head
    new_head = reverse_LL_rec(head.next,head)    # Here we are calling our reverse function again and again
    head.next = prev
    return new_head


if __name__ == "__main__": 

    head = Node(5)
    head.next = Node(15)
    head.next.next = Node(25)
    head.next.next.next = Node(35)

    printList(head)
    print()
    head_rev = reverse_LL_rec(head,None)
    printList(head_rev)











"""
Q-2 ) Write postorder and inorder traversal function for the tree given
below, including declaring classes, providing input and perform the dry run
also. (5 marks)
(Lengthy but easy)

"""





class Node:
    def __init__(self, data):   # Initialize and create an empty node
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:   # If our root is empty then come out of the function
        return
    
    inorder(root.left)   # Here we are calling our reverse function again and again
    print(root.data)
    inorder(root.right)  # Here we are calling our reverse function again and again

def postorder(root):
    if root is None:
        return
    
    postorder(root.left)  # Here we are calling our reverse function again and again
    postorder(root.right)  # Here we are calling our reverse function again and again
    print(root.data)

if __name__ == "__main__":

    root = Node(15)
    root.left = Node(11)
    root.right = Node(33)

    root.left.right = Node(66)
    root.left.left = Node(99)
    
    inorder(root)






"""
Q-3) N-ary Tree Preorder Traversal (5 marks)
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Given the root of an n-ary tree, return the preorder traversal of its nodes'
values.
pay attention, n is not defined. Write a code that can traverse a tree for any
value of “n” in “n-ary”.
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
explanation:
Input is top to bottom, left to right fashion.
first element root, will be followed by null.
3,2,4 are children of 1, followed by null means, children of 1 are over.
then 5,6 are children of 3.

"""





"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        if not root:
            return []

        tree = [root.val]
        if root.children:
            for child in root.children:
                tree += self.preorder(child)
        return tree


if __name__ == "__main__":

    Solution()




