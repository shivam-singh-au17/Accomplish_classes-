#!/bin/python3

import math
import os
import random
import re
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        
def NodesCount(head):
    count = 0
    while (head != None):
        head = head.next
        count += 1

    return count


def deleteMid(head):
    if (head == None):
        return None
    if (head.next == None):
        del head
        return None
    secondHade = head
    count = NodesCount(head)
    mid = count // 2
    while (mid > 1):
        mid -= 1
        head = head.next
    head.next = head.next.next

    return secondHade


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Llist:
    def __init__(self):
    	self.head=None
    def insert(self,data,tail):
        node=Node(data)
        if not self.head:
            self.head=node
            return node
        tail.next=node
        return node
def printList(head):
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr1=[int(x) for x in input().split()]
        ll=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll.insert(nodeData,tail)
        res=deleteMid(ll.head)
        printList(res)
