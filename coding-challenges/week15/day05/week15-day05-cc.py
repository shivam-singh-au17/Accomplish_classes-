

"""
Q-1 ) Gas station (Google interview problem)
https://leetcode.com/problems/gas-station/
(5 marks)
(Medium)
There are n gas stations along a circular route, where the amount of gas at the
ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from
the ith station to its next (i + 1)th station. You begin the journey with an empty
tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if
you can travel around the circuit once in the clockwise direction, otherwise return
-1. If there exists a solution, it is guaranteed to be unique
Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station
3.
Therefore, return 3 as the starting index.

"""





class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index





"""
Q-2) Maximum Units on a Truck (5 marks)
https://leetcode.com/problems/maximum-units-on-a-truck/
(Easy)
You are assigned to put some amount of boxes onto one truck. You are given a
2D array boxTypes, where boxTypes[i] = [numberOfBoxesi,
numberOfUnitsPerBoxi]:
● numberOfBoxesi is the number of boxes of type i.
● numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes
that can be put on the truck. You can choose any boxes to put on the truck as
long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third
type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

"""





class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1] , reverse=True)
                
        count = 0
        
        k = 0
        
        for i , j in boxTypes:
            if(truckSize < i):
                break
            
            count += i * j
            
            truckSize -= i
            
            k += 1
        
        try:
            return count + (truckSize * boxTypes[k][1])
        except:
            return count





"""
Q-3) Partition Equal Subset Sum
(5Marks)
(Medium)
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array
can be partitioned into two subsets such that the sum of elements in both
subsets is equal.
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""





class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for val in range(target,num-1,-1):
                dp[val] = dp[val] or dp[val-num]
        return dp[-1]




