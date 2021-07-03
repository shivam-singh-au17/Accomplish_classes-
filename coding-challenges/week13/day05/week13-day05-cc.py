


"""
Q-1 ) Q1. Represent a graph using adjacency list and adjacency matrix.
(5 marks)
(super-easy)
Don't just blindly copy the code, try to understand each line of code.

"""





class AdjNode:
	def __init__(self, data):
		self.vertex = data
		self.next = None

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None] * self.V

	def add_edge(self, src, dest):
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

	def print_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" {}".format(temp.vertex), end="")
				temp = temp.next
			print(" \n")



if __name__ == "__main__":
	V = 5
	graph = Graph(V)
	graph.add_edge(0, 1)
	graph.add_edge(0, 4)
	graph.add_edge(1, 2)
	graph.add_edge(1, 3)
	graph.add_edge(1, 4)
	graph.add_edge(2, 3)
	graph.add_edge(3, 4)

	graph.print_graph()





"""
Q-2 )Palindrome Number - Try using BFS in this (5 marks)
https://leetcode.com/problems/palindrome-number/
(Easy)
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For
example, 121 is palindrome while 123 is not.
Example 1:
Input: x = 121
Output: true
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

"""





class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        rev = 0
        temp = x
        while temp > 0:
            rev = (rev * 10) + (temp % 10)
            temp = temp // 10
        return rev == x





"""
Q-3 ) Binary Tree Zigzag Level Order Traversal (5 marks)
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
(Medium)
Given the root of a binary tree, return the zigzag level order traversal of its nodes'
values. (i.e., from left to right, then right to left for the next level and alternate
between).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
"""





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):

        l_to_r = True
        if not root: return
        queue = []
        queue.append(root)
        result = []

        while queue:

            length = len(queue)
            current_res = []
            for _ in range(length):

                if l_to_r:
                    current = queue.pop(0)
                    current_res.append(current.val)
                    if current.left: queue.append(current.left)
                    if current.right: queue.append(current.right)

                else:
                    current = queue.pop()
                    current_res.append(current.val)
                    if current.right: queue.insert(0, current.right)
                    if current.left: queue.insert(0, current.left)
            result.append(current_res)
            l_to_r = not l_to_r

        return result




