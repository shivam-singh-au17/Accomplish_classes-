


"""
Q-1 ) 4Sum
https://leetcode.com/problems/4sum/
(7.5 marks)
(Medium)
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
● 0 <= a, b, c, d < n
● a, b, c, and d are distinct.
● nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

"""





class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        i = 0
        L = len(nums)
        res = []
        while i < L-3:
            j = i+1
            while j < L-2:
                left = j+1
                right = L-1
                new_target = target-nums[i]-nums[j]
                while left<right:
                    if nums[left]+nums[right] > new_target:
                        right-=1
                    elif nums[left]+nums[right] < new_target:
                        left+=1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        temp_left = nums[left]
                        temp_right = nums[right]
                        while(left<right and nums[left]==temp_left):
                            left+=1
                        while(left<right and nums[right]==temp_right):
                            right-=1
                while j < L-3 and nums[j] == nums[j+1]:
                    j+=1
                j+=1
            while i < L-4 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res







"""
Q-2) Clone Graph (7.5 marks)
https://leetcode.com/problems/clone-graph/
(Medium)
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.
class Node {
public int val;
public List<Node> neighbors;
}
Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For
example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite
graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the
copy of the given node as a reference to the cloned graph.
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

"""






# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
       def cloneGraph(self, node: 'Node') -> 'Node':
            if node == None:
                return None

            vi = set()
            hm = {}

            def dfs(node, vi, hm):
                vi.add(node)
                copyNode = Node(node.val, [])
                hm[node] = copyNode

                for dest in node.neighbors:
                    if dest not in vi:
                        dfs(dest, vi, hm)

                    copyNode.neighbors.append(hm[dest])

            dfs(node, vi, hm)

            return hm[node]
        



