

"""
Q-1 ) LRU Cache (3.75 marks)
https://leetcode.com/problems/lru-cache/
(Medium)
Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.
Implement the LRUCache class:
● LRUCache(int capacity) Initialize the LRU cache with positive size
capacity.
● int get(int key) Return the value of the key if the key exists, otherwise
return -1.
● void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys
exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

"""





class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)  #Remove it first before inserting it at the end again
        self.dict[key] = val   
        return val        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:    
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]         
        self.dict[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





"""
Q-2 ) Flipping an Image (3.75 marks)
https://leetcode.com/problems/flipping-an-image/
(Easy)
Given an n x n binary matrix image, flip the image horizontally, then invert it, and
return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
● For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by
0.
● For example, inverting [0,1,1] results in [1,0,0].
Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

"""





class Solution:
    def flipAndInvertImage(self, image):
        
        arrInvert = []
        arrReverse = []
        for i in  image:
            i.reverse()
            arrInvert = []
            for j in i:
                if j == 0:
                    j = 1
                else:
                    j = 0
                arrInvert.append(j)
            arrReverse.append(arrInvert)
        return arrReverse





"""
Q-3) Richest Customer Wealth (3.75 marks)
https://leetcode.com/problems/richest-customer-wealth/
(Easy)
You are given an m x n integer grid accounts where accounts[i][j] is the amount of
money the ith customer has in the jth bank. Return the wealth that the richest
customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

"""





class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth  = -1
        for i in accounts:
            wealth  = max(wealth , sum(i))
        return wealth 
        




"""
Q-4) Remove Duplicates from Sorted List (3.75 marks)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
(Easy)
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]

"""






class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        while current!=None and current.next!=None:
            if current.val==current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head




"""
Q-5) [BONUS QUESTION] Search a 2D Matrix (3.75 marks)
(Medium)
https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
● Integers in each row are sorted from left to right.
● The first integer of each row is greater than the last integer of the
previous row.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

"""





class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
        start = 0
        end = len(matrix)
        
        if end == 0:
            return False
        
        while start < end:
            mid = (start + end) // 2
            
            s = 0
            e = len(matrix[mid])
        
            if e == 0:
                return False
            
            while s < e:
                m = (s+e)//2
                
                if matrix[mid][m] == target:
                    return True
                elif matrix[mid][m] < target:
                    s = m + 1
                else:
                    e = m
            
            if matrix[mid][0] > target:
                end = mid
            elif matrix[mid][-1] < target:
                start = mid + 1
            else:
                return False
        return False




