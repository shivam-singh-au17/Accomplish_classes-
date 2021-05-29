
"""
1480 Running Sum of 1d Array

"""


# nums = [1, 2, 3, 4]

# for i in range(1, len(nums)):
#     nums[i] += nums[i - 1]
# print(nums)
 


"""
1431. Kids With the Greatest Number of Candies

"""



# candies = [2,3,5,1,3]

# extraCandies = 3

# max = candies[0]
# for i in range(0, len(candies)):
#     if max < candies[i]:
#         max = candies[i]
# print(max)


# res = []
# for j in range(0, len(candies)):
#     if ((candies[j] + extraCandies) >= max):
#         res.append(True)
#     else:
#         res.append(False)
# print(res)


"""
1470. Shuffle the Array

"""



# nums = [2,5,1,3,4,7]
# n = 3

# arr = []
# for i in range(n):
#     arr += [nums[i], nums[i+3]]
# print(arr)


"""
1672. Richest Customer Wealth

"""



# accounts = [
#     [1,2,3],
#     [3,2,1]
#     ]


# mx = -1
# for i in accounts:
#     mx = max(mx, sum(i))

# print(mx)

a = [1,2,3,4]
t = 5

found = False

for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i] + a[j] == t:
      print(a[i],a[j])
      found = True
      break
  
  if found:
    break



        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
        # _dict = {}
        # for i, num in enumerate(nums):
        #     if target-num in _dict.keys():
        #         return [_dict[target-num], i]
        #     else:
        #         _dict[num] = i
                


arr = [1,2,3,4]

print(arr[::- 1])