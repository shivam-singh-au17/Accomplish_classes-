

"""
Q-1 ) Implement Queue using Stacks (5 marks)
https://leetcode.com/problems/implement-queue-using-stacks/
(5 marks)
(Easy)
Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue (push,
peek, pop, and empty).
Implement the MyQueue class:
● void push(int x) Pushes element x to the back of the queue.
● int pop() Removes the element from the front of the queue and returns it.
● int peek() Returns the element at the front of the queue.
● boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
● You must use only standard operations of a stack, which means only push
to top, peek/pop from top, size, and is empty operations are valid.
● Depending on your language, the stack may not be supported natively. You
may simulate a stack using a list or deque (double-ended queue) as long
as you use only a stack's standard operations.
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

"""





class MyQueue:

    def __init__(self):
    
        self.first = []
        self.last = []


    def push(self, x: int) -> None:
        
        length = len(self.first)
        for i in range(length):
            self.last.append(self.first.pop())
        self.last.append(x)
        

    def pop(self) -> int:
      
        length = len(self.last)
        for i in range(length):
            self.first.append(self.last.pop())
        return self.first.pop()


    def peek(self) -> int:
       
        if (len(self.last) > 0):
            return self.last[0]
        return self.first[len(self.first)-1]
        

    def empty(self) -> bool:
       
        if len(self.first) == 0 and len(self.last) == 0:
            return True
        return False


if __name__ == "__main__":

    MyQueue()





"""
Q-2 ) Palindrome Linked List (5 marks)
https://leetcode.com/problems/palindrome-linked-list/
(Easy)
5612
448
Add to List
Share
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false

"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def isPalindrome(self, head):
		temp = []
		while head != None:
			temp.append(head.val)
			head = head.next			
		if temp == temp[::-1]:
			return True
		else:
			return False


if __name__ == "__main__":

    Solution()





"""
Q-3) Maximum Depth of Binary Tree(or height of a BT): (5 marks)
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2

"""





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        q = deque()
        q.append(root)
        depth = 0
        while len(q) > 0:
            depth+=1
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
        return depth


if __name__ == "__main__":

    Solution()





"""
Q - 4) [BONUS QUESTION] Implement a stack, using two queues. (4
marks)

"""




