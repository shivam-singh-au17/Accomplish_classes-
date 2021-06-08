

"""
Q-1 ) Number of Good Pairs: (5 marks)
https://leetcode.com/problems/number-of-good-pairs/
Easy
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

"""





def GoodPairs(nums):
    dic = {}
    count = 0
    for num in nums:

        if num not in dic:
            dic[num] = 1
        elif num in dic:
            count += dic[num]
            dic[num] += 1
            
    return count


if __name__ == "__main__":

    nums = [1,2,3,1,1,3]
    ans = GoodPairs(nums)
    print(ans)
    




"""
Q-2 ) Jewels and StonesJewels and numStones: (5 marks)
https://leetcode.com/problems/jewels-and-stones/
You're given strings jewels representing the types of stones that are jewels, and
stones representing the stones you have. Each character in stones is a type of
stone you have. You want to know how many of the stones you have are also
jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

"""





def numStonesJewels(jewels, stones):
    numStones = {}
    numJewels = 0

    for i in stones:
        if i not in numStones:
            numStones[i] = 1
        else:
            numStones[i] += 1     

    for j in jewels:
        if j in numStones:
            numJewels += numStones[j]

    return numJewels


if __name__ == "__main__":

    jewels = "aA"
    stones = "aAAbbbb"
    ans = numStonesJewels(jewels, stones)
    print(ans)





"""
Q-3 ) How Many Numbers Are Smaller Than the Current Number: (5 marks)
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-cu
rrent-number/
Given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have to count the number of
valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exists one smaller number than it (1).
For nums[3]=2 there exists one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

"""






def smlNumThanCurr(nums):

    sortedArr = sorted(nums)
    dic = {}
    for i in range(len(sortedArr)):

        if sortedArr[i] not in dic:
            dic[sortedArr[i]] = i
            
    res = []
    
    for i in range(len(nums)):
        res.append(dic[nums[i]])
    
    return res


if __name__ == "__main__":

    nums = [8,1,2,2,3]
    ans = smlNumThanCurr(nums)
    print(ans)




