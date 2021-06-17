

"""
Q-1 ) Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
(5 marks)
(Medium)
Write a function to delete a node in a singly-linked list. You will not be given
access to the head of the list, instead you will be given access to the node
to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.
Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list
should become 4 -> 1 -> 9 after calling your function.

"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def deleteNode(self, node):

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        delElmt = node.next
        node.next = node.next.next

        del(delElmt)


if __name__ == "__main__" :

    head = [4,5,1,9]
    node = 5
    # Solution(node)    




"""
Q-2 )Remove Duplicates from Sorted List (5 marks)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
(Easy)
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def deleteDuplicates(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        while cur!=None and cur.next!=None:

            if cur.val==cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


if __name__ == "__main__" :

    head = [1,1,2,3,3]
    # Solution(head)    





"""
Q-3 ) Merge In Between Linked Lists (5 marks)
https://leetcode.com/problems/merge-in-between-linked-lists/
(Medium)
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their
place.
The blue edges and nodes in the following figure incidate the result:
Build the result list and return its head.
Example 1:
Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
place. The blue edges and nodes in the above figure indicate the result.

"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeInBetween(self, list1, a, b, list2):

        start = None
        end = list1
        for i in range(b):

            if i == a - 1:
                start = end
            end = end.next
        start.next = list2

        while list2.next:

            list2 = list2.next
        list2.next = end.next
        end.next = None

        return list1


if __name__ == "__main__" :

    list1 = [0,1,2,3,4,5] 
    a = 3
    b = 4
    list2 = [1000000,1000001,1000002]
    # Solution(list1, a, b, list2)    




