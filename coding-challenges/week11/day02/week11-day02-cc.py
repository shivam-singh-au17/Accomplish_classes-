

"""
Q-1 ) Write a program to remove first node from a linked list:
(5 marks)
(Super Easy)
Example 1:
Input(elements in linked list)
2
5
6
8
3
Output(elements after removing head of the linked list)
5
6
8
3

"""





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None

def addNodeAtEnd(x):
    global head

    if head is None:
        head = Node(x)
        return
    
    cur = head
    while cur.next != None:
        cur = cur.next
    
    cur.next = Node(x)


def printLinkedList():
    global head

    cur = head
    while cur != None:
        print(cur.data)
        cur = cur.next


def deleteAtHead():
    global head
    if head is None:
        return

    head = head.next


if __name__ == "__main__":

    addNodeAtEnd(2)
    addNodeAtEnd(5)
    addNodeAtEnd(6)
    addNodeAtEnd(8)
    addNodeAtEnd(3)
    
    deleteAtHead()
    printLinkedList()
    




"""
Q-2 ) Convert Binary Number in a Linked List to Integer: (5 marks)
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
(Easy)
Given head which is a reference node to a singly-linked list. The value of each
node in the linked list is either 0 or 1. The linked list holds the binary
representation of a number.
Return the decimal value of the number in the linked list.
Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def getDecimalValue(head):
    temp = head
    node = 0
    while (temp):
        node += 1
        temp = temp.next
    result = 0
    for i in range(node):
        result += head.val * 2 ** (node - 1 - i)
        head = head.next
    return result


if __name__ == "__main__":

    head = [1,0,1]
    ans = getDecimalValue(head)
    print(ans)




"""
Q-3 ) Middle of the Linked List (5 marks)
https://leetcode.com/problems/middle-of-the-linked-list/
(Medium)
Given a non-empty, singly linked list with head node head, return a middle node
of linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3. (The judge's serialization of this node is
[3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
= NULL.

"""





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = head.next
    fast = head.next
    
    if not head or head.next is None:
        return head
    
    while slow is not None and fast.next is not None and fast.next.next is not None:
        
        slow = slow.next
        fast = fast.next.next
        
    return slow


if __name__ == "__main__":

    head = [1,2,3,4,5]
    ans = middleNode(head)
    print(ans)





