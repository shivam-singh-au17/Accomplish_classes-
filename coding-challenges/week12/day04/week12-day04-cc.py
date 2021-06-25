

"""
Q-1 ) Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
(5 marks)
(Medium)
Given an integer array nums and an integer k, return the kth largest element in
the array.
Note that it is the kth largest element in the sorted order, not the kth distinct
element.
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""





class Solution:

    def findKthLargest(self, nums, k):
        if not nums or not k or k < 0:
            return None

        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)

            else:
                if num > minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, num)

        return minheap[0]





"""
Q-2 )Kth Largest Element in a Stream (5 marks)
https://leetcode.com/problems/kth-largest-element-in-a-stream/
(Easy)
Design a class to find the kth largest element in a stream. Note that it is the
kth largest element in the sorted order, not the kth distinct element.
Implement KthLargest class:
● KthLargest(int k, int[] nums) Initializes the object with the integer k
and the stream of integers nums.
● int add(int val) Returns the element representing the kth largest
element in the stream.
Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]
Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

"""





class KthLargest:

    def __init__(self, k, nums):

        self.heap = []
        self.k = k

        for i in nums:

            if len(self.heap) < k:
                heapq.heappush(self.heap,i)

            else:

                if i > self.heap[0]:
                    heapq.heappushpop(self.heap,i)
        

    def add(self, val):

        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)

        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap,val)   

        return self.heap[0]





"""
Q-3 )Minimum Cost of ropes (5 marks)
https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/
1
(Easy)
There are given N ropes of different lengths, we need to connect these ropes into
one rope. The cost to connect two ropes is equal to sum of their lengths. The
task is to connect the ropes with minimum cost.
Example 1:
Input:
n = 4
arr[] = {4, 3, 2, 6}
Output:
29
Explanation:
For example if we are given 4
ropes of lengths 4, 3, 2 and 6. We can
connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3.
Now we have three ropes of lengths 4, 6
and 5.
2) Now connect ropes of lengths 4 and 5.
Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all
ropes have connected.
Total cost for connecting all ropes is 5
+ 9 + 15 = 29. This is the optimized cost
for connecting ropes. Other ways of
connecting ropes would always have same
or more cost. For example, if we connect
4 and 6 first (we get three strings of 3,
2 and 10), then connect 10 and 3 (we get
two strings of 13 and 2). Finally we
connect 13 and 2. Total cost in this way
is 10 + 13 + 15 = 38.

"""





import heapq

def minCost(arr, n):
	
	heapq.heapify(arr)
	res = 0

	while(len(arr) > 1):

		first = heapq.heappop(arr)
		second = heapq.heappop(arr)

		res += first + second
		heapq.heappush(arr, first + second)
		
	return res

if __name__ == '__main__':
	
	lengths = [ 4, 3, 2, 6 ]
	size = len(lengths)
	
	print("Total cost for connecting ropes is " + str(minCost(lengths, size)))




